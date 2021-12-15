#file = 'input12_test.txt'
file = 'input12.txt'

with open(f'inputs/{file}') as f:
    contents = f.readlines()

connections = [(x.strip().split('-')[0],x.strip().split('-')[1]) for x in contents]

# Python program to print all paths from a source to destination.

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
# Part of the class code is contributed by Dr. Neelam Yadav, which I adjusted for advent_of_code_2021 (lines marked with #DF)
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # No. of paths
        self.path_count = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def AllPathsUtil(self, u, d, visited, path, option):
        # Mark the current node as visited if lowercase and store in path
        if u == u.lower():
            visited[u]= True #DF
        path.append(u) #DF

        # If current vertex is same as destination, then print
        # current path[]
        if u == d and option == 'print':#DF
            print(path)
            self.path_count+=1#DF
        elif u == d and option == 'count':#DF
            self.path_count+=1#DF
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.AllPathsUtil(i, d, visited, path, option)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False


    # Prints all paths from 's' to 'd'
    def AllPaths(self, s, d, option='count'):
        visited = {}
        # Mark all the vertices as not visited
        for i in self.V:
            visited[i] = False
        # Create an array to store paths
        path = []

        # Call the recursive helper function to count all paths
        self.AllPathsUtil(s, d, visited, path, option)


# --------------DF---------
nodes = set()
for conn in connections:
    for item in conn:
        nodes.add(item)

# Create a graph given in the above diagram
#g = Graph(len(nodes))
g = Graph(sorted(nodes))

for conn in connections:
    if 'start' in conn:
        if 'start' in conn[0]: g.addEdge(conn[0],conn[1])
        else: g.addEdge(conn[1],conn[0])
    elif 'end' in conn:
        if 'end' in conn[0]: g.addEdge(conn[1],conn[0])
        else: g.addEdge(conn[0],conn[1])
    else:
        g.addEdge(conn[0],conn[1])
        g.addEdge(conn[1],conn[0])
#---------DF------------

s = 'start' ; d = 'end'
# option 1 is used for either just counting ('count') or counting and printing all the paths ('print'). The default is to count
# --Solution 1--
g.AllPaths(s, d)
print (f"Solution 1: {g.path_count}")
