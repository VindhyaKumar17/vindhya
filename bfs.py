    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_detect_cycle(self, start):
        visited = set()
        parent = {start: None}
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
                elif parent[node] != neighbor:
                    return True
        return False

    def has_cycle(self):
        visited = set()
        for node in self.graph:
            if node not in visited:
                if self.bfs_detect_cycle(node):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

if g.has_cycle():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")