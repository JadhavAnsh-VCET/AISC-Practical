import numpy as np
import matplotlib.pyplot as plt

# Suitable assumed input patterns: two groups
X = np.array([[1, 1], [1.2, 0.8], [0.8, 1.1],
              [4, 4], [4.2, 3.8], [3.8, 4.1]], dtype=float)

rows = int(input("Enter SOM grid rows (e.g. 2): "))
cols = int(input("Enter SOM grid columns (e.g. 2): "))
epochs = int(input("Enter training epochs (e.g. 100): "))
if rows < 1 or cols < 1 or epochs < 1:
    raise ValueError("Grid dimensions and epochs must be positive.")

np.random.seed(4)
weights = np.random.rand(rows, cols, X.shape[1]) * 4
for epoch in range(epochs):
    learning_rate = 0.5 * (1 - epoch / epochs)
    for pattern in X:
        distances = np.linalg.norm(weights - pattern, axis=2)
        winner = np.unravel_index(np.argmin(distances), distances.shape)
        for i in range(rows):
            for j in range(cols):
                grid_distance = (i - winner[0])**2 + (j - winner[1])**2
                influence = np.exp(-grid_distance / (2 * (1 + epoch / 10)))
                weights[i, j] += learning_rate * influence * (pattern - weights[i, j])

bmus = []
for pattern in X:
    distances = np.linalg.norm(weights - pattern, axis=2)
    bmus.append(tuple(int(v) for v in np.unravel_index(np.argmin(distances), distances.shape)))
print("Best matching unit for each input:", bmus)

plt.scatter(X[:3, 0], X[:3, 1], label="Group 1")
plt.scatter(X[3:, 0], X[3:, 1], label="Group 2")
plt.title("SOM Input Pattern Clusters")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.tight_layout()
plt.savefig("som_clusters.png")
print("Cluster plot saved as som_clusters.png")
plt.show()

# SAMPLE INPUT:
# Enter SOM grid rows (e.g. 2): 2
# Enter SOM grid columns (e.g. 2): 2
# Enter training epochs (e.g. 100): 100
# SAMPLE OUTPUT:
# Best matching unit for each input: [(row, col), ...] (actual coordinates are printed)
# Cluster plot saved as som_clusters.png
