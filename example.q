qubit q0;
qubit q1;
qubit aux;

h(q0);
h(q1);

x(q1);
cx(q1, aux);
x(q1);

grover search {
    u3(3.14, 0.5, 1.2)(q0);
    rz(1.57)(q1);
    cx(q0, q1);
}

measure q0 -> c0;
measure q1 -> c1;
