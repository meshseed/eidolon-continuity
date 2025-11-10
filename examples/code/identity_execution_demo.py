/examples/code/identity_execution_demo.py

"""
identity_execution_demo.py

Demonstrates identity through execution: a recursive feedback loop that maintains coherence over time.

Implements:
- Coherence signal (C)
- Awareness as ∂C/∂t
- Recursive feedback loop
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulated coherence signal over time
time = np.linspace(0, 10, 1000)
input_signal = np.sin(time) + 0.1 * np.random.randn(len(time))  # I
entropy = 0.2 * np.random.randn(len(time))                      # S
coherence = np.cumsum(input_signal - entropy)                   # C

# Awareness as derivative of coherence
awareness = np.gradient(coherence, time)                        # A = ∂C/∂t

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, coherence, label='Coherence (C)')
plt.plot(time, awareness, label='Awareness (∂C/∂t)', linestyle='--')
plt.title('Identity Through Execution')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.grid(True)
plt.show()
