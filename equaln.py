#Group 3
#Anushka Gupta (agupta35)
#Sreeraj Rajendran (srajend2)
#Varun Garg (vsgarg)


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute
import numpy as np

n = 5
qx = QuantumRegister(2*n)
cx = ClassicalRegister(2*n)
qextra = QuantumRegister(n-1)
cextra = ClassicalRegister(n-1)
qz = QuantumRegister(1)
cz = ClassicalRegister(1)
circuit = QuantumCircuit(qextra,qx,qz,cextra,cx,cz)


a=np.zeros((2*n))
for i in range(n) :
	a[i] = int (input ('Enter input 1,bit ' + str(i)+ ': '))
for i in range(n) :
	a[i+n] = int (input ('Enter input 2,bit ' + str(i) + ': '  ))
for i in range(2*n):
    if a[i]==1:
        circuit.x(qx[i])

for i in range(n) :
	circuit.cx(qx[i],qx[i+n])
	circuit.x(qx[i+n])

circuit.ccx(qx[n], qx[n+1], qextra[0])
for i in range(1,n-1) :
	circuit.ccx(qx[i+n+1], qextra[i-1], qextra[i])

circuit.cx(qextra[n-2], qz[0])

for i in range(n-2,0,-1) :
	circuit.ccx(qx[i+n+1], qextra[i-1], qextra[i])

circuit.ccx(qx[n], qx[n+1], qextra[0])

for i in range(n) :
	circuit.cx(qx[i],qx[i+n])
	circuit.x(qx[i+n])


circuit.measure(qextra, cextra)
circuit.measure(qx,cx)
circuit.measure(qz,cz)

print(circuit.qasm())

# Execute
print("Running on simulator...")
backend = 'local_qasm_simulator'
job = execute(circuit, backend, shots=128)
result = job.result()
print()
print()
print("Output format")
print("Output of equality check | Input qubit 2 and input qubit 1 | Extra qubits used for computation but recovered before measurement | Number of shots")
print(result.get_counts(circuit))