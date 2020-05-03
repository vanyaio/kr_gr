# Python3 program for Bellman-Ford's single source  
# shortest path algorithm.  
  
# Class to represent a graph  
class Graph:  
  
    def __init__(self):  
        self.graph = []  
        self.v = set()
  
    # function to add an edge to graph  
    def addEdge(self, u, v, w):  
        self.graph.append([u, v, w])  
        self.v.add(u)
        self.v.add(v)
          
    # utility function used to print the solution  
    def printArr(self, dist):  
        print("Vertex Distance from Source")  
        for i in range(self.V):  
            print("{0}\t\t{1}".format(i, dist[i]))  
      
    # The main function that finds shortest distances from src to  
    # all other vertices using Bellman-Ford algorithm. The function  
    # also detects negative weight cycle  
    def BellmanFord(self, src):  
  
        # Step 1: Initialize distances from src to all other vertices  
        # as INFINITE  
        #  dist = [float("Inf")] * self.V  
        dist = {}
        dist_ans = {}
        parent = {}
        for v in self.v:
            dist[v] = float("Inf")
            parent[v] = None
            dist_ans[v] = []
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest  
        # path from src to any other vertex can have at-most |V| - 1  
        # edges 
        print(len(self.v))
        for _ in range(len(self.v) - 1):  
            # Update dist value and parent index of the adjacent vertices of  
            # the picked vertex. Consider only those vertices which are still in  
            # queue  
            print('hello', _)
            any = False
            for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                    any = True
                    dist[v] = dist[u] + w  
                    parent[v] = u
            if not any:
                break
            for v in self.v:
                dist_ans[v].append((_, dist[v]))

        print(dist_ans)
        print(parent)
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        #  for u, v, w in self.graph:  
                #  if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        #  print("Graph contains negative weight cycle") 
                        #  return
                          
        # print all distance  
        #  self.printArr(dist)  
  
g = Graph()  
g.addEdge('s', 'a', 7)  
g.addEdge('s', 'c', 6)  
g.addEdge('s', 'f', 5)  
g.addEdge('s', 'e', 6)  
g.addEdge('a', 'b', 4)  
g.addEdge('a', 'c', -2)  
g.addEdge('c', 'd', 2)  
g.addEdge('c', 'f', 1)  
g.addEdge('f', 'd', 3)  
g.addEdge('b', 'g', -2)  
g.addEdge('b', 'h', -4)  
g.addEdge('e', 'h', 3)  
g.addEdge('e', 'f', -2)  
g.addEdge('h', 'g', 1)  
g.addEdge('g', 'i', -1)  
g.addEdge('i', 'h', 1)  
  
# Print the solution  
g.BellmanFord('s')  
  
# Initially, Contributed by Neelam Yadav  
# Later On, Edited by Himanshu Garg 
