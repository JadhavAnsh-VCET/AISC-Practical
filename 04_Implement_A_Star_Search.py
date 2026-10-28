import heapq

graph = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "D": 3, "E": 2},
    "C": {"A": 3, "F": 2, "G": 3},
    "D": {"B": 3, "H": 3},
    "E": {"B": 2, "H": 4},
    "F": {"C": 2, "H": 3},
    "G": {"C": 3, "H": 2},
    "H": {"D": 3, "E": 4, "F": 3, "G": 2},
}
heuristic = {"A": 5, "B": 4, "C": 3, "D": 3, "E": 3, "F": 2, "G": 1, "H": 0}

def a_star(start, goal):
    frontier = [(heuristic[start], 0, start, [start])]
    best_g = {start: 0}
    while frontier:
        _, g_cost, node, path = heapq.heappop(frontier)
        if node == goal:
            return path, g_cost
        if g_cost != best_g.get(node):
            continue
        for neighbor, edge_cost in graph[node].items():
            new_g = g_cost + edge_cost
            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                heapq.heappush(frontier, (new_g + heuristic[neighbor], new_g,
                                          neighbor, path + [neighbor]))
    return None, float("inf")

start = input("Enter start node (A-H): ").strip().upper()
goal = input("Enter goal node (A-H): ").strip().upper()
if start not in graph or goal not in graph:
    print("Invalid node. Use A through H.")
else:
    path, cost = a_star(start, goal)
    print("A* path:", " -> ".join(path) if path else "No path found")
    print("Total path cost:", cost)

# SAMPLE INPUT:
# Enter start node (A-H): A
# Enter goal node (A-H): H
# SAMPLE OUTPUT:
# A* path: A -> C -> G -> H
# Total path cost: 8
# NOTE: Other optimal routes of cost 8 may appear due to tie-breaking.
