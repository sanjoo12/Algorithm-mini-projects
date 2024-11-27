from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            queue.extend(graph[vertex] - visited)
    
    return traversal

def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(graph[vertex] - visited)
    
    return traversal

if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print("BFS Traversal:", bfs(graph, 'A'))
    print("DFS Traversal:", dfs(graph, 'A'))
