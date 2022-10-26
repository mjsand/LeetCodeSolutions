import collections
from collections import defaultdict

#this solution is going to implement a directed graph to find the shortest paths between origin and destination

class Graph(object):

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    #adds connections to our graph
    def add_connections(self, connections):

        for node1, node2 in connections:
            self.add(node1, node2)

    #adds connection between node1 and node2
    def add(self, node1, node2):

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    #removes references to node
    def remove(self, node):

        for n, cxns in self._graph.items():  
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass
    
    #determines if node1 and node2 are directly connected
    def is_connected(self, node1, node2):

        return node1 in self._graph and node2 in self._graph[node1]

    #this function will find any path between 2 nodes if it exists
    def find_path(self, node1, node2, path=[]):

        path = path + [node1]
        paths = []
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    paths.append(new_path)

        return paths

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
    
#this function will clean the output from find_path and return the proper output
def cleanPath(paths):
    #first we will check for empty input
    if paths == [] or paths is None:
        return 'none'
    else:
        return paths
    
    
    
#this function will create our connections, a list of tuples, from the flights string input
def determineConnections(flights):
    connections = []
    #split up the flight paths
    flightPaths = flights.split(" ")
    #now we will iterate over flightPaths, remove the hyphens by splitting, then iterate over that new string object and create a tuple for each connection
    #then we add each connection to our array, connections, and return it
    for i in flightPaths:
        path = i.split("-")
        for j in range(len(path)-1):
            connection = (path[j], path[j+1])
            connections.append(connection)

    return connections


#we initialize our flight paths
flights = "NY-Iceland-London-Berlin NY-Maine-London Berlin-Paris-Amsterdam Paris-London-Egypt"
origin = "NY"
destination = "London"
#create our connections list of tuples and then generate our directed graph
connections = determineConnections(flights)
flightGraph = Graph(connections, directed=True)


#the following are some test cases that will determine if we receive our expected output

### Test 1
origin1 = "NY"
dest1 = "London"
paths1 = flightGraph.find_path(origin1, dest1)
cp1 = cleanPath(paths1)
#we expect to have 2 paths returned from NY to London of the same length
print(cp1)
if len(cp1) == 2:
    print(len(cp1), "unique paths were found between " + origin1 + " and " + dest1 + ".")

### Test 2
origin2 = "Boston"
dest2 = "London"
paths2 = flightGraph.find_path(origin2, dest2)
cp2 = cleanPath(paths2)
#we expect to return the string none since Boston is not in our flight paths
if cp2 == 'none':
    print(cp2)
    print("No paths were found between " + origin2 + " and " + dest2 + ".")

### Test 3
origin3 = "NY"
dest3 = "Egypt"
paths3 = flightGraph.find_path(origin3, dest3)
cp3 = cleanPath(paths3)
#we expect to return 2 unique paths between NY and Egypt of the same length
print(cp3)
if len(cp3) == 2:
    print(len(cp3), "unique paths were found between " + origin3 + " and " + dest3 + ".")