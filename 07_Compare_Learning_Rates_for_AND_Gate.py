import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1], dtype=float)

def sigmoid(value):
    return 1 / (1 + np.exp(-np.clip(value, -50, 50)))

def train(learning_rate, max_epochs):
    weights = np.array([0.1, -0.1], dtype=float)  # same initial weights each run
    bias = -0.2
    for epoch in range(1, max_epochs + 1):
        for inputs, target in zip(X, y):
            output = sigmoid(np.dot(inputs, weights) + bias)
            delta = (target - output) * output * (1 - output)
            weights += learning_rate * delta * inputs
            bias += learning_rate * delta
        predicted = (sigmoid(X @ weights + bias) >= 0.5).astype(int)
        if np.array_equal(predicted, y.astype(int)):
            return epoch, weights, bias, predicted
    return max_epochs, weights, bias, predicted

max_epochs = int(input("Enter maximum epochs (e.g. 50000): "))
for rate in [0.1, 0.3, 0.5]:
    epochs_used, weights, bias, predicted = train(rate, max_epochs)
    print(f"Learning rate {rate}: epochs={epochs_used}, predictions={predicted.tolist()}, "
          f"weights={np.round(weights, 3)}, bias={bias:.3f}")

# SAMPLE INPUT:
# Enter maximum epochs (e.g. 50000): 50000
# SAMPLE OUTPUT:
# Learning rate 0.1: epochs=<measured by program>, predictions=[0, 0, 0, 1], ...
# Learning rate 0.3: epochs=<measured by program>, predictions=[0, 0, 0, 1], ...
# Learning rate 0.5: epochs=<measured by program>, predictions=[0, 0, 0, 1], ...
# The exact epoch counts and parameter values are printed by your run.
