graph = {
    'A': {'B': 6, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 8}
}
def dijkstra(start):
    dist = {}
    visited = []
    for node in graph:
        dist[node] = float('inf')
    dist[start] = 0
    
    while len(visited) < len(graph):
        # Find minimum distance node
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or dist[node] < dist[min_node]:
                    min_node = node
        
        visited.append(min_node)
        for neighbor in graph[min_node]:
            if neighbor not in visited:
                new_dist = dist[min_node] + graph[min_node][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
    return dist

result = dijkstra('A')
print("Shortest distances from A:", result)