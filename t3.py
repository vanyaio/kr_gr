from collections import defaultdict

#This class represents a directed graph using adjacency matrix representation
class Graph:

    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        #self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)

        # Create a queue for BFS
        queue=[]

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

         # Standard BFS Loop
        while queue:

            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 

            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            print("path flow", path_flow)
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                print((u,v),self.graph[u][v],(v,u),self.graph[v][u])
                v = parent[v]

        gr_len = len(self.graph)
        map = {}
        for i in range(gr_len):
            map[i] = []

        for v, arr in enumerate(self.graph): 
            for u, c in enumerate(self.graph[v]):
                if (c != 0):
                    map[v].append((u, c))
        print(map)
        return max_flow
  
   
# Create a graph given in the above diagram 
#  graph = [
        #  [0, 16, 13, 0, 0, 0],
        #  [0, 0, 10, 12, 0, 0],
        #  [0, 4, 0, 0, 14, 0],
        #  [0, 0, 9, 0, 0, 20],
        #  [0, 0, 0, 7, 0, 4],
        #  [0, 0, 0, 0, 0, 0]
        #  ]
gr_len = 10
graph = []
for i in range(gr_len):
    arr = [0 for j in range(gr_len)]
    graph.append(arr)
map = {
    0 : [(1, 1), (2, 1), (4, 5), (3, 5)], \
    1 : [(3, 4), ], \
    2 : [(4, 2),], \
    3 : [(4, 2), (2, 2), (6,6)], \
    4 : [(5, 3), (6, 3)], \
    5 : [(8, 8), (7, 2), (3, 2)], \
    6 : [(5, 2), (7, 7), (8, 2)], \
    7 : [(9, float('inf'))], \
    8 : [(9, float('inf'))], \
       }
for v in map:
    for p in map[v]:
        u = p[0]
        c = p[1]
        graph[v][u] = c
print(graph)
g = Graph(graph)
source = 0; sink = 9
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
