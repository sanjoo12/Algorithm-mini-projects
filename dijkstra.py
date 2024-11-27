import heapq

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    shortest_path = {}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path[neighbor] = current_vertex

    return distances, shortest_path

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 3},
        'D': {'B': 2},
        'E': {'B': 5, 'F': 1},
        'F': {'C': 3, 'E': 1}
    }
    distances, paths = dijkstra(graph, 'A')
    print("Shortest distances from A:", distances)
