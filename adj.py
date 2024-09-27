#create a class named as graph
# using adjacency list
class Graph:
    # create constructor function
    def __init__(self):
        self.graph={}
        self.directed=False
    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def AddEdge (self,src,dest):
        self.AddVertex(src)
        self.AddVertex(dest)
        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)
    def displayGraph(self):
        for vertex in self.graph:
            print(f"{vertex}->{self.graph[vertex]}")
G=Graph()
G.AddEdge('A','B')
G.AddEdge('A','C')
G.AddEdge('A','D')
G.AddEdge('B','D')
G.AddEdge('C','F')
G.AddEdge('C','D')
G.AddEdge('D','E')
G.AddEdge('E','F')
G.displayGraph()

