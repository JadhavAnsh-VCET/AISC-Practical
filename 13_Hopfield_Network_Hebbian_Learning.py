import numpy as np

# Bipolar stored patterns (-1 and +1)
patterns = np.array([[1, -1, 1, -1], [-1, 1, -1, 1]], dtype=int)
n = patterns.shape[1]
weights = np.zeros((n, n), dtype=float)

# Hebbian learning
for pattern in patterns:
    weights += np.outer(pattern, pattern)
np.fill_diagonal(weights, 0)
weights /= n

binary = input("Enter a noisy 4-bit binary pattern (e.g. 1110): ").strip()
if len(binary) != 4 or any(bit not in "01" for bit in binary):
    raise ValueError("Enter exactly four binary digits, such as 1110.")

state = np.array([1 if bit == "1" else -1 for bit in binary], dtype=int)
print("Input pattern (bipolar):", state.tolist())
for _ in range(10):
    previous = state.copy()
    for i in range(n):
        net_input = np.dot(weights[i], state)
        state[i] = 1 if net_input >= 0 else -1
    if np.array_equal(state, previous):
        break

recalled_binary = "".join("1" if bit == 1 else "0" for bit in state)
print("Recalled pattern (bipolar):", state.tolist())
print("Recalled pattern (binary):", recalled_binary)

# SAMPLE INPUT:
# Enter a noisy 4-bit binary pattern (e.g. 1110): 1110
# SAMPLE OUTPUT:
# Recalled pattern (binary): 1010
# NOTE: Recall depends on the stored patterns and the amount of noise.
