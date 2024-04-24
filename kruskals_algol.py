'''
This program implements the Kruskals Algorithm to find the minimum spanning
tree. It will read data from a file, if no file name is given it will default
to testDataB.txt.
'''
import constants as co
import prims_algol as prims

'''
This program is the kruskals minimal spanning tree algorithm. It takes in data
from a file and returns the data as a set type. In the set it will contain the
data in the format of (node1, node2) where node1 is the source and node2 is the
target.
    Args:
        -edgeList: list of edges in pairs of tuples read from a file
        -n: total nodes in the graph
        -edges: total edges that exists in the graph
'''
def kruskals(edgeList, n, edges):
    edgeList = sorted(edgeList)
    MST = set()
    GV = dict()
    for x in range(n):
        GV[x + 1] = x + 1
    x = 0

    while len(MST) != n-1:
        weight, u, v = edgeList[x]
        x += 1
        
        v1 = searchMST(GV, u)
        v2 = searchMST(GV, v)
        
        if v1 != v2:
            MST = MST | {(u, v)}
            GV[v1] = GV[v2]

    return MST

'''
Allows to search linked keys in the dictionary to find all related nodes.
    Args:
        -GV: dictionary containing each node and its connected nodes
        -node: a node that is passed to determine connectivity
'''
def searchMST(GV, node):
    x = node

    while GV[x] != x:
        x = GV[x]
    
    return x
'''
This function is necessary to build the graph as a 2D array so that when the
data is displayed it has the O(1) access for each individual edge. Any node
pair not given defaults to the INFINITE value.
    Args:
        -edgeList: list of all edges with their weights
        -n: total nodes in the graph
'''
def buildGraph(edgeList, n):
    graph = [['X' for x in range(n)] for x in range(n)]
    for weight, x, y in edgeList:
        graph[x - 1][y - 1] = weight
        graph[y - 1][x - 1] = weight

    for x in range(n):
        graph[x][x] = 0
    return graph

'''
Parses the file based on certain criteria. It will return the three values:
graph, nodes, edges; Each value is necessary to create the graph and impliment
the algorithm.
    Args:
        -file: a file that can be specified by the user otherwise it defaults
            to testFileB.txt
'''
def parseFile(file=co.TESTB):
    f = open(file, 'r')
    graph = []

    temp = f.readline()
    temp = temp.strip('\n')

    i = 0
    while temp[i] != ' ':
        i += 1
    nodes = int(temp[:i])
    edges = int(temp[i + 1:])
    
    for line in f:
        temp = line.strip('\n')
        i = temp.find(' ')
        node1 = int(temp[:i])
        temp = temp[i+1:]

        i = temp.find(' ')
        node2 = int(temp[:i])
        weight = int(temp[i + 1:])
        
        val = (weight, node1, node2)
        graph.append(val)
    
    return graph, nodes, edges
