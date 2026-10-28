import numpy as np

# Training data from the practical PDF
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1], dtype=float).reshape(-1, 1)

x1 = int(input("Enter first test feature x1 (0 or 1): "))
x2 = int(input("Enter second test feature x2 (0 or 1): "))
epochs = int(input("Enter training epochs (e.g. 15000): "))
learning_rate = float(input("Enter learning rate (e.g. 0.8): "))
if x1 not in (0, 1) or x2 not in (0, 1):
    raise ValueError("Test features must be 0 or 1.")

test = np.array([[x1, x2]], dtype=float)
np.random.seed(7)
W1 = np.random.randn(2, 3) * 0.5
b1 = np.zeros((1, 3))
W2 = np.random.randn(3, 1) * 0.5
b2 = np.zeros((1, 1))

def sigmoid(value):
    return 1 / (1 + np.exp(-np.clip(value, -50, 50)))

for _ in range(epochs):
    hidden = sigmoid(X @ W1 + b1)
    output = sigmoid(hidden @ W2 + b2)
    output_delta = (output - y) * output * (1 - output)
    hidden_delta = (output_delta @ W2.T) * hidden * (1 - hidden)
    W2 -= learning_rate * (hidden.T @ output_delta) / len(X)
    b2 -= learning_rate * np.mean(output_delta, axis=0, keepdims=True)
    W1 -= learning_rate * (X.T @ hidden_delta) / len(X)
    b1 -= learning_rate * np.mean(hidden_delta, axis=0, keepdims=True)

probability = sigmoid(sigmoid(test @ W1 + b1) @ W2 + b2)[0, 0]
print("Test input:", (x1, x2))
print("Output probability:", round(float(probability), 3))
print("Predicted class:", int(probability >= 0.5))

# SAMPLE INPUT:
# x1 = 0
# x2 = 1
# Enter training epochs (e.g. 15000): 15000
# Enter learning rate (e.g. 0.8): 0.8
# SAMPLE OUTPUT:
# Predicted class is printed above (0 or 1).
# Loan target table is AND logic; (1,1) should classify as Approved (1).
