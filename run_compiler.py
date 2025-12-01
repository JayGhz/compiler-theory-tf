from quantum_compiler import QuantumLLVMCompiler
import sys
import os

def main():
    # Directorio de salida
    output_dir = "/output"
    
    if len(sys.argv) < 2:
        print("Uso: python run_compiler.py <archivo.q>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        source_code = f.read()
    
    print(f"Compilando: {input_file}")
    print("="*50)
    
    compiler = QuantumLLVMCompiler()
    compiler.compile(source_code)
    qc, counts = compiler.execute(shots=1024)
    
    # Guardar LLVM IR
    llvm_path = os.path.join(output_dir, 'out.ll')
    with open(llvm_path, 'w') as f:
        f.write(compiler.get_llvm_ir())
    
    print(f"\nLLVM IR guardado en: {llvm_path}")
    

if __name__ == '__main__':
    main()