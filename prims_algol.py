'''
This file implements the Prim's Algorithm to find minimal spanning tree. It will
recieve data froma file. If the file name is not specified by the user it will
default to testDataA.txt.
'''
import constants as co


'''
This function is used to determine the smallest edge closest to any of the
current nodes within the nodeSet argument. It then updates nodeList and
returns the edge as a tuple.
    Args:
        -graph: graph containing all of the edges
        -nodeSet: set of currently found nodes
        -nodeList: list of all possible nodes
'''
def smallestEdge(graph, nodeSet, nodeList, n):
    minCost = co.INFINITE
    t = 0
    for u in range(n):
        if (u + 1) in nodeSet:
            for v in range(n):
                if ((v+1) not in nodeSet):
                    if minCost == co.INFINITE:
                        minCost = graph[u][v]
                        t = (u + 1,v + 1)
                    elif graph[u][v] != co.INFINITE and minCost > graph[u][v]:
                        minCost = graph[u][v]
                        t = (u + 1,v + 1)
    nodeList.remove(t[1])
    return t

'''
A python version of the prims algorithm. It will return a set containing all
of the shortest edges in the graph.
    Args:
        -graph: graph containing edges
        -n: total nodes in the graph
'''
def prims(graph, n):
    # Resulting nodes with edges
    T = set()
    U = { 1 }
    nodes = [ x + 1 for x in range(n)]
    while len(U) != n:
        u, v = smallestEdge(graph, U, nodes, n)
        T = T | {(u,v)}
        U = U | {v}

    return T

'''
Parses the file and produces the resulting graph from the file.
    Args:
        -file: defaults to testDataA.txt, otherwise searches the file of
            the user's choice.
'''
def parseFile(file=co.TESTA):
    f = open(file, 'r')
    n = int(f.readline())
    i = 0
    graph = [ [] for x in range(n) ]
    
    for line in f:
        temp = ""
        for char in line:
            if char == ' ':
                try:
                    graph[i].append(int(temp))
                    temp = ""
                except ValueError:
                    pass
            elif char == co.INFINITE:
                graph[i].append(char)
            else:
                temp += char
        try:
            graph[i].append(int(temp))
        except ValueError:
            pass

        i += 1

    return graph, n
