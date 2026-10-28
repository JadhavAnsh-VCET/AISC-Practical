import numpy as np

# Truth-table patterns for the AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1], dtype=float)

learning_rate = float(input("Enter learning rate (e.g. 0.5): "))
epochs = int(input("Enter maximum epochs (e.g. 20000): "))

np.random.seed(1)
weights = np.random.uniform(-0.2, 0.2, 2)
bias = 0.0

def sigmoid(value):
    return 1 / (1 + np.exp(-np.clip(value, -50, 50)))

for _ in range(epochs):
    for inputs, target in zip(X, y):
        output = sigmoid(np.dot(inputs, weights) + bias)
        delta = (target - output) * output * (1 - output)
        weights += learning_rate * delta * inputs
        bias += learning_rate * delta

probabilities = sigmoid(X @ weights + bias)
predictions = (probabilities >= 0.5).astype(int)
print("Final weights:", np.round(weights, 3))
print("Final bias:", round(float(bias), 3))
print("Predictions:", predictions.tolist())
print("Targets:    ", y.astype(int).tolist())
print("All patterns classified correctly:", bool(np.array_equal(predictions, y.astype(int))))

# SAMPLE INPUT:
# Enter learning rate (e.g. 0.5): 0.5
# Enter maximum epochs (e.g. 20000): 20000
# SAMPLE OUTPUT:
# Predictions: [0,0,0,1]
# Targets:     [0,0,0,1]
# All patterns classified correctly: True
# NOTE: Learned weights and bias are printed; exact decimals can vary.
