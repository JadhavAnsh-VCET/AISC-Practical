import numpy as np

# Assumed example dataset: XOR classification
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

learning_rate = float(input("Enter learning rate (e.g. 0.8): "))
epochs = int(input("Enter training epochs (e.g. 20000): "))
hidden_neurons = int(input("Enter number of hidden neurons (e.g. 4): "))

np.random.seed(2)
W1 = np.random.randn(2, hidden_neurons) * 0.5
b1 = np.zeros((1, hidden_neurons))
W2 = np.random.randn(hidden_neurons, 1) * 0.5
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

probabilities = sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2).ravel()
print("Predicted probabilities:", np.round(probabilities, 3).tolist())
print("Predicted classes:", (probabilities >= 0.5).astype(int).tolist())
print("Target classes:   ", y.astype(int).ravel().tolist())

# SAMPLE INPUT:
# Enter learning rate (e.g. 0.8): 0.8
# Enter training epochs (e.g. 20000): 20000
# Enter number of hidden neurons (e.g. 4): 4
# SAMPLE OUTPUT:
# Predicted classes: [0, 1, 1, 0]
# Target classes:    [0, 1, 1, 0]
# NOTE: Training settings affect the exact probabilities.
