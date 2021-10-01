class DisjointSets:
            def __init__(self, vertex):
                self.vertex=vertex 
                self.parent={}
                for v in vertex:
                    self.parent[v]=v
                self.rank=dict.fromkeys(vertex,0)
                
            def find(self, item):
                if (self.parent[item]== item):
                    return item
                else:
                    return(self.find(self.parent[item]))
                
            def union(self, x, y):
                xroot=self.parent[x]
                yroot=self.parent[y]
                
                if(self.rank[xroot]<self.rank[yroot]):
                    self.parent[xroot]=yroot
                    
                elif(self.rank[xroot]>self.rank[yroot]):
                    self.parent[yroot]=xroot
                
                else:
                    self.parent[yroot]=xroot
                    self.rank[xroot]+=1
                    
class Graph:
    def __init__(self, vertex):
        self.V=vertex
        self.graph=[]
        self.nodes=[]
        self.MST=[]
        
    def addEdge(self, s, d, weight):
        self.graph.append([s, d, weight])
        
    def addNode(self, value):
        self.nodes.append(value)
        
    def printSolution(self, s, d,w):
        for s, d ,w in self.MST:
            print("%s - %s: %s" %(s,d,w))

    def kruskal(self):
        i, e=0,0
        ds=DisjointSets(self.nodes)
        self.graph=sorted(self.graph, key=lambda item:item[2])
        while e<self.V-1:
            s,d,w=self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(d)
            if x !=y:
                e+=1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)
        
g=Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.addEdge("A", "B",5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D",8 )
g.addEdge("A", "C",13)
g.addEdge("C", "D", 6)
g.addEdge("E", "A",15 )
g.addEdge("C", "E",20 )

g.kruskal()
