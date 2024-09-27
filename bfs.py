def bfs(graph, start):
    visited = []   
    queue = []     
    visited.append(start)
    queue.append(start)
    while queue:
        vertex = queue.pop(0)  
        print(vertex, end=" ") 
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)  
                queue.append(neighbor)    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


bfs(graph, 'A')