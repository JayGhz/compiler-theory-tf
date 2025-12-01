from antlr4 import *
from QuantumParser import QuantumParser
from QuantumVisitor import QuantumVisitor
from llvmlite import ir, binding as llvm
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumLLVMCompiler(QuantumVisitor):
    """
    Compilador híbrido:
    - Frontend: ANTLR4 (parsing)
    - Middle-end: LLVM IR (optimización)
    - Backend: Qiskit (ejecución cuántica)
    """
    
    def __init__(self):
        # LLVM Module
        self.module = ir.Module(name="quantum_module")
        self.builder = None
        self.func_type = ir.FunctionType(ir.VoidType(), [])
        self.main_func = ir.Function(self.module, self.func_type, name="main")
        
        # Qiskit structures
        self.qubit_map = {}
        self.classical_map = {}
        self.instructions = []
        
        # LLVM variables
        self.llvm_vars = {}
        
    def compile(self, input_code):
        """Punto de entrada principal"""
        # 1. Parse con ANTLR
        input_stream = InputStream(input_code)
        lexer = QuantumLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = QuantumParser(tokens)
        tree = parser.prog()
        
        # 2. Crear bloque de entrada LLVM
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        
        # 3. Visitar AST
        self.visit(tree)
        
        # 4. Finalizar función LLVM
        self.builder.ret_void()
        
        return tree
    
    def visitQubitDecl(self, ctx):
        """Declarar qubit"""
        name = ctx.ID().getText()
        idx = len(self.qubit_map)
        self.qubit_map[name] = idx
        
        # LLVM: Alocar qubit como array [real, imag]
        qubit_type = ir.ArrayType(ir.DoubleType(), 2)
        qubit_ptr = self.builder.alloca(qubit_type, name=f"qubit_{name}")
        
        # Inicializar a |0⟩ = [1.0, 0.0]
        zero_val = ir.Constant(ir.DoubleType(), 0.0)
        one_val = ir.Constant(ir.DoubleType(), 1.0)
        
        idx0 = ir.Constant(ir.IntType(32), 0)
        idx1 = ir.Constant(ir.IntType(32), 1)
        
        ptr_real = self.builder.gep(qubit_ptr, [idx0, idx0])
        ptr_imag = self.builder.gep(qubit_ptr, [idx0, idx1])
        
        self.builder.store(one_val, ptr_real)
        self.builder.store(zero_val, ptr_imag)
        
        self.llvm_vars[name] = qubit_ptr
        
        self.instructions.append({
            'type': 'declare_qubit',
            'name': name
        })
        
        return self.visitChildren(ctx)
    
    def visitApplyGateStmt(self, ctx):
        """Aplicar gate cuántico"""
        gate_ctx = ctx.applyGate()
        gate_name = gate_ctx.gate().getText()
        
        # Extraer targets
        targets = []
        if gate_ctx.argList():
            for arg in gate_ctx.argList().arg():
                if arg.ID():
                    targets.append(arg.ID().getText())
        
        # Si hay segundo paréntesis con idList
        if gate_ctx.idList():
            targets = [id_node.getText() for id_node in gate_ctx.idList().ID()]
        
        # Extraer parámetros numéricos
        params = []
        if gate_ctx.argList():
            for arg in gate_ctx.argList().arg():
                if arg.expr():
                    # Evaluar expresión (simplificado)
                    params.append(arg.expr().getText())
        
        # Emitir llamada LLVM
        self._emit_gate_llvm(gate_name, targets, params)
        
        # Guardar para Qiskit
        self.instructions.append({
            'type': 'gate',
            'gate': gate_name,
            'targets': targets,
            'params': params
        })
        
        return self.visitChildren(ctx)
    
    def _emit_gate_llvm(self, gate_name, targets, params):
        """Emitir código LLVM para gate cuántico"""
        # Declarar función externa (runtime)
        func_name = f"quantum_gate_{gate_name}"
        
        # Tipo: void gate_fn(double* qubit, ...)
        qubit_ptr_type = ir.PointerType(ir.ArrayType(ir.DoubleType(), 2))
        
        # Número de qubits objetivo
        n_targets = len(targets)
        
        # Agregar parámetros float si existen
        arg_types = []
        for _ in params:
            arg_types.append(ir.DoubleType())
        for _ in targets:
            arg_types.append(qubit_ptr_type)
        
        fn_type = ir.FunctionType(ir.VoidType(), arg_types)
        
        # Declarar función
        if func_name not in self.module.globals:
            gate_fn = ir.Function(self.module, fn_type, name=func_name)
        else:
            gate_fn = self.module.get_global(func_name)
        
        # Preparar argumentos
        call_args = []
        
        # Agregar parámetros
        for p in params:
            try:
                param_val = float(p)
                call_args.append(ir.Constant(ir.DoubleType(), param_val))
            except:
                # Variable (no implementado en este ejemplo)
                pass
        
        # Agregar punteros a qubits
        for target in targets:
            if target in self.llvm_vars:
                call_args.append(self.llvm_vars[target])
        
        # Llamar función
        self.builder.call(gate_fn, call_args)
    
    def visitMeasureStmt(self, ctx):
        """Measurement"""
        src = ctx.ID(0).getText()
        dst = ctx.ID(1).getText()
        
        if dst not in self.classical_map:
            idx = len(self.classical_map)
            self.classical_map[dst] = idx
        
        self.instructions.append({
            'type': 'measure',
            'src': src,
            'dst': dst
        })
        
        return self.visitChildren(ctx)
    
    def visitGroverBlock(self, ctx):
        """Bloque Grover"""
        name = ctx.ID().getText()
        
        # Comentario LLVM
        self.builder.comment(f"Begin Grover block: {name}")
        
        self.instructions.append({
            'type': 'grover_start',
            'name': name
        })
        
        # Visitar contenido
        result = self.visitBlock(ctx.block())
        
        self.instructions.append({
            'type': 'grover_end',
            'name': name
        })
        
        self.builder.comment(f"End Grover block: {name}")
        
        return result
    
    def get_llvm_ir(self):
        """Retornar LLVM IR como string"""
        return str(self.module)
    
    def build_qiskit_circuit(self):
        """Construir circuito Qiskit desde IR"""
        n_qubits = len(self.qubit_map)
        n_clbits = len(self.classical_map)
        
        qc = QuantumCircuit(n_qubits, n_clbits)
        
        for instr in self.instructions:
            if instr['type'] == 'gate':
                gate = instr['gate'].lower()
                targets = [self.qubit_map[t] for t in instr['targets'] 
                          if t in self.qubit_map]
                params = instr.get('params', [])
                
                if gate == 'h' and targets:
                    qc.h(targets[0])
                elif gate == 'x' and targets:
                    qc.x(targets[0])
                elif gate == 'y' and targets:
                    qc.y(targets[0])
                elif gate == 'z' and targets:
                    qc.z(targets[0])
                elif gate == 'cx' and len(targets) >= 2:
                    qc.cx(targets[0], targets[1])
                elif gate == 'cz' and len(targets) >= 2:
                    qc.cz(targets[0], targets[1])
                elif gate == 'ccx' and len(targets) >= 3:
                    qc.ccx(targets[0], targets[1], targets[2])
                elif gate == 'u3' and len(params) >= 3 and targets:
                    theta = float(params[0])
                    phi = float(params[1])
                    lam = float(params[2])
                    qc.u(theta, phi, lam, targets[0])
                elif gate == 'rz' and len(params) >= 1 and targets:
                    qc.rz(float(params[0]), targets[0])
                elif gate == 'rx' and len(params) >= 1 and targets:
                    qc.rx(float(params[0]), targets[0])
                elif gate == 'ry' and len(params) >= 1 and targets:
                    qc.ry(float(params[0]), targets[0])
            
            elif instr['type'] == 'measure':
                src_idx = self.qubit_map[instr['src']]
                dst_idx = self.classical_map[instr['dst']]
                qc.measure(src_idx, dst_idx)
        
        return qc
    
    def execute(self, shots=1024):
        """Ejecutar circuito cuántico"""
        qc = self.build_qiskit_circuit()
        
        print("=== LLVM IR Generado ===")
        print(self.get_llvm_ir())
        print("\n" + "="*50 + "\n")
        
        print("=== Circuito Cuántico ===")
        print(qc.draw(output='text'))
        print("\n" + "="*50 + "\n")
        
        # Simular
        sim = AerSimulator()
        result = sim.run(qc, shots=shots).result()
        counts = result.get_counts()
        
        print("=== Resultados de Medición ===")
        print(counts)
        
        plot_histogram(counts)
        plt.savefig('/output/results.png')
        print("\nGráfico guardado en: /output/results.png")
        
        return qc, counts


from QuantumLexer import QuantumLexer