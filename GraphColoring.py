N = 4
# Adjacency matrix representation of the graph
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3 # Number of available colors

# Array to track the color assigned to each node (0 means uncolored)
colors = [0] * N

def solve(node):
    # Base case: If all nodes are assigned a color
    if node == N:
        print("Solution found (colors):", colors)
        return
        
    for c in range(1, m + 1):
        # Branch & Bound check: Check constraints before proceeding (Bounding)
        # Verify adjacent nodes to ensure no color conflict
        is_safe = True
        for neighbor in range(N):
            if graph[node][neighbor] == 1 and colors[neighbor] == c:
                is_safe = False
                break
                
        if is_safe:
            # Assign the color
            colors[node] = c
            
            # Recursion (Branching)
            solve(node + 1)
            
            # Backtrack
            colors[node] = 0

print(f"Graph Coloring Solutions (for {N} nodes using {m} colors):")
solve(0)
