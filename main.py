
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt
import random

qc = QuantumCircuit(4, 3)
coin = 0
pos = [1, 2, 3]

for step in range(3):
    qc.h(coin)
    qc.rz(0.4 * (step + 1), coin)

    if random.random() < 0.1:
        print(f"Step {step+1}: Coin decided to flip itself! 😂")
        qc.x(coin)

    for i, p in enumerate(pos):
        qc.cx(coin, p)
        qc.crz(0.2 * (i + 1), coin, p)

    qc.cz(pos[0], pos[1])
    qc.cz(pos[1], pos[2])

qc.h(coin)
for p in pos:
    qc.h(p)

qc.measure(pos, [0, 1, 2])

# Save circuit diagram
circuit_drawer(qc, output='mpl', filename='outputs/circuit.png')

backend = Aer.get_backend('qasm_simulator')
result = backend.run(qc, shots=1024).result()
counts = result.get_counts()

plot_histogram(counts)
plt.savefig("outputs/histogram.png")
plt.show()

print(counts)
