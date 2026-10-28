import heapq

graph = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"],
    "D": ["H"], "E": ["H"], "F": ["H"], "G": ["H"], "H": [],
}
heuristic = {"A": 6, "B": 4, "C": 3, "D": 2, "E": 3, "F": 2, "G": 1, "H": 0}

def greedy_best_first(start, goal):
    frontier = [(heuristic[start], start, [start])]
    visited = set()
    while frontier:
        _, node, path = heapq.heappop(frontier)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

start = input("Enter start node (A-H): ").strip().upper()
goal = input("Enter goal node (A-H): ").strip().upper()
if start not in graph or goal not in graph:
    print("Invalid node. Use A through H.")
else:
    path = greedy_best_first(start, goal)
    print("Greedy Best-First path:", " -> ".join(path) if path else "No path found")

# SAMPLE INPUT:
# Enter start node (A-H): A
# Enter goal node (A-H): H
# SAMPLE OUTPUT:
# Greedy Best-First path: A -> C -> G -> H
