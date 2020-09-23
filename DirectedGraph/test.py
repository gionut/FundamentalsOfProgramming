import unittest
from DirectedGraph import DirectedGraph
class MyTestCase(unittest.TestCase):
    def test_get_graph_from_file(self):
        with open("graph.txt", "r")as f:
            firstLine = f.readline()
            firstLine = firstLine.split()
            nrVertices = int(firstLine[0])
            nrEdges = int(firstLine[1])

        graph = DirectedGraph(nrVertices, nrEdges)
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

        self.assertEqual(nrVertices, 5)
        self.assertEqual(graph.isEdge(1, 2), 1)
        self.assertEqual(graph.isEdge(0, 4), 0)

        self.assertEqual(graph.getInDegree(1), 2)
        self.assertEqual(graph.getOutDegree(3), 0)

        self.assertEqual(graph.parseOutboundEdges(0), [(0,0), (0,1)])

        self.assertEqual(graph.parseInboundEdges(1), [(0,1), (2,1)])

        graph.removeEdge((0, 1))
        self.assertEqual(graph.getNrEdges(), 5)
        self.assertEqual(graph.parseOutboundEdges(0), [(0, 0)])
        self.assertEqual(graph.parseInboundEdges(1), [(2, 1)])

        graph.addEdge(0, 1, 7);

        graph.removeVertex(2)
        self.assertEqual(graph.getNrEdges(), 3)
        self.assertEqual(graph.getNrVertices(), 4)

        print("\n")
        for vertex in vertices:
            print(vertex)
            print(graph.parseNin(vertex))
            print(graph.parseNout(vertex))
            print("\n")

        edges = graph.parseEdges()
        for edge in edges:
            print(str(edge) + " - " + str(edges[edge]))

        self.assertEqual(graph.getCost((0, 1)), 7)

        graph.modifyCost((0,1), 5)
        self.assertEqual(graph.getCost((0,1)), 5)

        copyOfGraph = graph.copyGraph()
        copyOfGraph.modifyCost((0,1), 7)

        self.assertEqual(copyOfGraph.getCost((0,1)), 7)
        self.assertEqual(graph.getCost((0,1)), 5)

        randomGraph = graph.randomGraph(10,14)
        randomGraph.writeGraphToFile("randomgraph.txt")

if __name__ == '__main__':
    unittest.main()
