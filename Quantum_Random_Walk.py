"""
Quantum Random Walk with a Funny Twist ⚛️🎲

Author: Aqeel Ahmad
Description:
This script implements a Quantum Random Walk using Qiskit.
It uses:
- 1 coin qubit
- 3 position qubits
- Quantum entanglement and interference
- A playful classical randomness twist
"""

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt
import random

# Create quantum circuit
qc = QuantumCircuit(4, 3)

coin = 0
pos = [1, 2, 3]

# Quantum Random Walk (3 steps)
for step in range(3):
    # Quantum coin flip
    qc.h(coin)
    qc.rz(0.4 * (step + 1), coin)

    # Funny classical randomness
    if random.random() < 0.1:
        print(f"Step {step+1}: Coin flipped itself 😂")
        qc.x(coin)

    # Conditional shift (entanglement)
    for i, p in enumerate(pos):
        qc.cx(coin, p)
        qc.crz(0.2 * (i + 1), coin, p)

    # Extra entanglement between position qubits
    qc.cz(pos[0], pos[1])
    qc.cz(pos[1], pos[2])

# Final superposition
qc.h(coin)
for p in pos:
    qc.h(p)

# Measurement
qc.measure(pos, [0, 1, 2])

# Draw circuit
circuit_drawer(qc, output="mpl")
plt.show()

# Run simulation
backend = Aer.get_backend("qasm_simulator")
result = backend.run(qc, shots=1024).result()
counts = result.get_counts()

# Plot results
plot_histogram(counts)
plt.show()

print("Measurement Results:")
print(counts)
