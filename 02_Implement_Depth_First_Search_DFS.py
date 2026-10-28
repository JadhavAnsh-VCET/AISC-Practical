graph = {
    "A": ["B", "C"],
    "B": ["O", "E"],
    "O": [],
    "E": ["H"],
    "H": [],
    "C": ["F", "G"],
    "F": [],
    "G": [],
}

def dfs_path(graph, node, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    visited.add(node)
    path = path + [node]
    if node == goal:
        return path
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path, visited)
            if result:
                return result
    return None

start = input("Enter start node (A, B, C, O, E, F, G, H): ").strip().upper()
goal = input("Enter goal node (A, B, C, O, E, F, G, H): ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid node. Check the nodes shown in the prompt.")
else:
    path = dfs_path(graph, start, goal)
    print("DFS path:", " -> ".join(path) if path else "No path found")

# SAMPLE INPUT:
# Enter start node (A, B, C, O, E, F, G, H): A
# Enter goal node (A, B, C, O, E, F, G, H): G
# SAMPLE OUTPUT:
# DFS path: A -> C -> G
# NOTE: The PDF's diagram labels the left child of B as O (letter O).
