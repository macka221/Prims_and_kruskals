import prims_algol as prims
import kruskals_algol as kruskal
import constants as co


def promptFileName():
    fileName = str(input("Enter a file name without '.txt'" +
                "\n *Click enter for default to a test file*) -> "))
    return fileName + ".txt"

def chooseAlgorithm():
    print(" Algorithm Choice \n" +
        "-------------------------")
    print(" 1) Prims Algorithm \n" +
          " 2) Kruskals Algorithm\n")
    choice = int(input("Enter your choice -> "))
    
    return co.algol[choice - 1]

def getNewGraphData(graph, nodes):
    print("Edges : Weights")
    print("-------------------")
    
    for x, y in nodes:
        edge = str(x) + '--' + str(y)
        weight = str(graph[x-1][y-1])
        print(edge + ' : ' + weight)




def __main__():
    pass

if __name__ == "__main__":
    fileName = promptFileName()
    algol = chooseAlgorithm()
    if fileName == ".txt":
        if algol == 'prims':
            graph, nodes = prims.parseFile()
            E = prims.prims(graph, nodes)
        else:
            edgeList, nodes, edges = kruskal.parseFile()
            graph = kruskal.buildGraph(edgeList, nodes)
            E = kruskal.kruskals(edgeList, nodes, edges)
    else:
        if algol == 'prims':
            graph, nodes = prims.parseFile(fileName)
            E = prims.prims(graph, nodes)
        else:
            edgeList, nodes, edges = kruskal.parseFile(fileName)
            graph = kruskal.buildGraph(edgeList, nodes)
            E = kruskal.kruskals(edgeList, nodes, edges)
    
    getNewGraphData(graph, E)
