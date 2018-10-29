#Group 3
#Anushka Gupta (agupta35)
#Sreeraj Rajendran (srajend2)
#Varun Garg (vsgarg)


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute
import numpy as np

number_of_qubits = 6


n = int(number_of_qubits/2)

qx = QuantumRegister(2*n)
cx = ClassicalRegister(2*n)
qextra = QuantumRegister(n-1)
cextra = ClassicalRegister(n-1)
qz = QuantumRegister(1)
cz = ClassicalRegister(1)
circuit = QuantumCircuit(qz,qextra,qx,cz,cextra,cx)


circuit.h(qx)
circuit.x(qz)
circuit.h(qz)
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

circuit.h(qz)
print(circuit.qasm())

print("Running on simulator...")
backend = 'local_statevector_simulator'
job = execute(circuit, backend)
result = job.result()
#print(result.get_counts(circuit))
statevector = np.round(result.get_statevector(circuit),3)

def printVector(v):
	for i in range(2**9):
		index = "{:09b}".format(i) 
		print(index, v[i])

printVector(statevector)
