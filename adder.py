#Group 3
#Anushka Gupta (agupta35)
#Sreeraj Rajendran (srajend2)
#Varun Garg (vsgarg)

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute
from qiskit.tools.visualization import matplotlib_circuit_drawer as drawer, qx_color_scheme
from qiskit.tools.visualization import circuit_drawer
n = 3
qx = QuantumRegister(n)
cx = ClassicalRegister(n)
qz = QuantumRegister(2)
cz = ClassicalRegister(2)
circuit = QuantumCircuit(qx,qz,cx,cz)
circuit.x(qx[0])
#circuit.x(qx[1])
circuit.x(qx[2])
'''
circuit.ccx(qx[0],qx[1],qz[1])
circuit.ccx(qx[1],qx[2],qz[1])
circuit.ccx(qx[0],qx[2],qz[1])
circuit.cx(qx[0],qz[0])
circuit.cx(qx[1],qz[0])
circuit.cx(qx[2],qz[0])
'''

for i in range(n-1,-1,-1):
    circuit.cx(qx[i],qz[0])
    for j in range(i-1,-1,-1):
        circuit.ccx(qx[i],qx[j],qz[1])



circuit.measure(qz,cz)
circuit.measure(qx,cx)

print(circuit.qasm())

# Execute
print("Running on simulator...")
backend = 'local_qasm_simulator'
job = execute(circuit, backend, shots=1024)
result = job.result()
print(result.get_counts(circuit))
#circuit_drawer(circuit)