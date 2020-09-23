import copy
import random
from random import randint

class DirectedGraph:
    def __init__(self, nrVertices, nrEdges):
        self.__nrVertices = nrVertices
        self.__nrEdges = nrEdges
        self._dictOut = {}  # create an empty dictionary for the Out vertices
        self._dictIn = {}  # create an empty dictionary for the In vertices
        self._dictCosts = {}
        for i in range(nrVertices):
            self._dictOut[i] = []  # create an empty list for each vertex
            self._dictIn[i] = []

    def parseVertices(self):
        return self._dictOut.keys()  # returns an iterable containing all the vertices

    def parseEdges(self):
        return self._dictCosts

    def parseNin(self, vertex):
        return self._dictIn[vertex]  # returns an iterable containing all the in vertices for the vertex "vertex"

    def parseNout(self, vertex):
        return self._dictOut[vertex]  # return an iterable containing all the out vertices for the vertex "vertex"

    def isEdge(self, outVertex, inVertex):
        if not self.isVertex(outVertex) or not self.isVertex(inVertex):  # check if the vertices exist
            raise ValueError("One of the vertices does not exist!\n")
        return inVertex in self._dictOut[outVertex]  # check if "outVertex" is an out vertex for the vertex "inVertex"  so if there is an edge from outVertex to invertex

    def isVertex(self, vertex):
        return vertex in self._dictOut.keys()  # check if the vertex "vertex" exists

    def addEdge(self, outVertex, inVertex, cost):
        if self.isEdge(outVertex, inVertex):
            raise ValueError("The edge does already exist!\n")  # check if the edge does not already exists
        self._dictOut[outVertex].append(inVertex)
        self._dictIn[inVertex].append(outVertex)
        self._dictCosts[(outVertex, inVertex)] = cost

    def getGraphFromFile(self, fileName):
        with open(fileName, "r") as f:
            f.readline()
            for i in range(self.__nrEdges):
                line = f.readline()
                line = line.split()
                outVertex = int(line[0])
                inVertex = int(line[1])
                cost = int(line[2])
                self.addEdge(outVertex, inVertex, cost)

    def writeGraphToFile(self, fileName):
        with open(fileName, "w") as f:
            line = ''
            line = line + str(self.getNrVertices()) + " " + str(self.getNrEdges()) + '\n'
            f.write(line)
            for edge in self._dictCosts:
                line = ''
                line = line + str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(self.getCost(edge)) + '\n'
                f.write(line)

    def getNrVertices(self):
        self.__nrVertices = len(self._dictIn)
        return self.__nrVertices

    def getInDegree(self, vertex):
        if self.isVertex(vertex):
            return len(self._dictIn[vertex])
        print("There is no such vertex!")

    def getOutDegree(self, vertex):
        if self.isVertex(vertex):
            return len(self._dictOut[vertex])
        print("There is no such vertex!")

    def parseOutboundEdges(self, vertex):
        outBoundEdges = []
        for edge in self._dictCosts.keys():
            if edge[0] == vertex:
                outBoundEdges.append(edge)
        return outBoundEdges

    def parseInboundEdges(self, vertex):
        outInEdges = []
        for edge in self._dictCosts.keys():
            if edge[1] == vertex:
                outInEdges.append(edge)
        return outInEdges

    def getNrEdges(self):
        return len(self._dictCosts.keys())

    def removeEdge(self, edge_id):
        if not self.isEdge(edge_id[0], edge_id[1]):
            print("There is no such an edge!")
            return
        inVertex = edge_id[1]
        outVertex = edge_id[0]
        self._dictOut[outVertex].remove(inVertex)
        self._dictIn[inVertex].remove(outVertex)
        del self._dictCosts[edge_id]

    def removeVertex(self, vertex_id):
        #outboundEdges = self.parseOutboundEdges(vertex_id)
        #inBoundEdges = self.parseInboundEdges(vertex_id)
        if not self.isVertex(vertex_id):
            print("There is no such vertex!")
            return

        for inVertex in self._dictOut[vertex_id]:
                del self._dictCosts[(vertex_id, inVertex)]
                self._dictIn[inVertex].remove(vertex_id)

        del self._dictOut[vertex_id]

        for outVertex in self._dictIn[vertex_id]:
            del self._dictCosts[(outVertex, vertex_id)]
            self._dictOut[outVertex].remove(vertex_id)

        del self._dictIn[vertex_id]

    def getCost(self, edge_id):
        return self._dictCosts[edge_id]

    def modifyCost(self, edge_id, newCost):
        self._dictCosts[edge_id] = newCost

    def copyGraph(self):
        copyOfGraph = copy.deepcopy(self);
        return copyOfGraph

    def randomGraph(self, nrVertices, nrEdges):
        randomGraph = DirectedGraph(nrVertices,nrEdges)
        vertices = []
        for vertex in range(nrVertices):
            vertices.append(int(vertex))
        for i in range(nrEdges):
            outVertex = inVertex = -1
            edge = ()
            while(outVertex == inVertex):
                outVertex = random.choice(vertices)
                inVertex = random.choice(vertices)
            if((outVertex, inVertex) in randomGraph._dictCosts.keys()):
                i = i-1
            else:
                randomGraph.addEdge(outVertex, inVertex, randint(-1000,1000))
        return randomGraph

with open("graph.txt", "r")as f:
    firstLine = f.readline()
    firstLine = firstLine.split()
    nrVertices = int(firstLine[0])
    nrEdges = int(firstLine[1])

graph = DirectedGraph(nrVertices, nrEdges)

#graph = graph.randomGraph(10,14)
#graph.writeGraphToFile("randomgraph.txt")
graph.getGraphFromFile("graph.txt")
graph.writeGraphToFile("graphOut.txt")

vertices = graph.parseVertices()
for vertex in vertices:
    print(vertex)
    print(graph.parseNin(vertex))
    print(graph.parseNout(vertex))
    print("\n")

edges = graph.parseEdges()
for edge in edges:
    print(str(edge) + " - " + str(edges[edge]))




