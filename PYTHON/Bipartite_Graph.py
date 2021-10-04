from collections import deque
 
 
# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
 
            # add an edge from source to destination
            self.adjList[src].append(dest)
 
            # add an edge from destination to source
            self.adjList[dest].append(src)
 
 
# Perform BFS on a graph starting from vertex `v`
def BFS(graph, v, N):
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
 
    # stores the level of each vertex in BFS
    level = [None] * N
 
    # mark the source vertex as discovered and set its level to 0
    discovered[v] = True
    level[v] = 0
 
    # create a queue to do BFS and enqueue source vertex
    q = deque()
    q.append(v)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and print it
        v = q.popleft()
 
        # do for every edge `v —> u`
        for u in graph.adjList[v]:
            # if vertex `u` is explored for the first time
            if not discovered[u]:
                # mark it as discovered
                discovered[u] = True
 
                # set level one more than the level of the parent node
                level[u] = level[v] + 1
 
                # enqueue vertex
                q.append(u)
 
            # if the vertex has already been discovered and the
            # level of vertex `u` and `v` are the same, then the
            # graph contains an odd-cycle and is not bipartite
            elif level[v] == level[u]:
                return False
 
    return True
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram.
    # Note that if we add edge `2 —> 4`, the graph becomes non-bipartite
    edges = [(1, 2), (2, 3), (2, 8), (3, 4), (4, 6), (5, 7), (5, 9), (8, 9)]
 
    # total number of nodes in the graph
    N = 10
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # Perform BFS traversal starting from vertex 1
    if BFS(graph, 1, N):
        print("The graph is bipartite")
    else:
        print("The graph is not bipartite")
