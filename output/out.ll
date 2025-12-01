; ModuleID = "quantum_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %"qubit_q0" = alloca [2 x double]
  %".2" = getelementptr [2 x double], [2 x double]* %"qubit_q0", i32 0, i32 0
  %".3" = getelementptr [2 x double], [2 x double]* %"qubit_q0", i32 0, i32 1
  store double 0x3ff0000000000000, double* %".2"
  store double              0x0, double* %".3"
  %"qubit_q1" = alloca [2 x double]
  %".6" = getelementptr [2 x double], [2 x double]* %"qubit_q1", i32 0, i32 0
  %".7" = getelementptr [2 x double], [2 x double]* %"qubit_q1", i32 0, i32 1
  store double 0x3ff0000000000000, double* %".6"
  store double              0x0, double* %".7"
  %"qubit_aux" = alloca [2 x double]
  %".10" = getelementptr [2 x double], [2 x double]* %"qubit_aux", i32 0, i32 0
  %".11" = getelementptr [2 x double], [2 x double]* %"qubit_aux", i32 0, i32 1
  store double 0x3ff0000000000000, double* %".10"
  store double              0x0, double* %".11"
  call void @"quantum_gate_h"([2 x double]* %"qubit_q0")
  call void @"quantum_gate_h"([2 x double]* %"qubit_q1")
  call void @"quantum_gate_x"([2 x double]* %"qubit_q1")
  call void @"quantum_gate_cx"([2 x double]* %"qubit_q1", [2 x double]* %"qubit_aux")
  call void @"quantum_gate_x"([2 x double]* %"qubit_q1")
  ; Begin Grover block: search
  call void @"quantum_gate_u3"(double 0x40091eb851eb851f, double 0x3fe0000000000000, double 0x3ff3333333333333, [2 x double]* %"qubit_q0")
  call void @"quantum_gate_rz"(double 0x3ff91eb851eb851f, [2 x double]* %"qubit_q1")
  call void @"quantum_gate_cx"([2 x double]* %"qubit_q0", [2 x double]* %"qubit_q1")
  ; End Grover block: search
  ret void
}

declare void @"quantum_gate_h"([2 x double]* %".1")

declare void @"quantum_gate_x"([2 x double]* %".1")

declare void @"quantum_gate_cx"([2 x double]* %".1", [2 x double]* %".2")

declare void @"quantum_gate_u3"(double %".1", double %".2", double %".3", [2 x double]* %".4")

declare void @"quantum_gate_rz"(double %".1", [2 x double]* %".2")
