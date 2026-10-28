from collections import deque

graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "E"],
    "C": ["B", "E", "F", "G"],
    "D": ["A", "E"],
    "E": ["A", "B", "C", "D", "F"],
    "F": ["C", "E", "G"],
    "G": ["C", "F"],
}

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

start = input("Enter start node (A-G): ").strip().upper()
goal = input("Enter goal node (A-G): ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid node. Use A, B, C, D, E, F, or G.")
else:
    path = bfs_path(graph, start, goal)
    print("BFS path:", " -> ".join(path) if path else "No path found")

# SAMPLE INPUT:
# Enter start node (A-G): A
# Enter goal node (A-G): G
# SAMPLE OUTPUT:
# BFS path: A -> B -> C -> G
