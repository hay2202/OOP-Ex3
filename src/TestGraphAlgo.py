import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def graph_creator():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 8, 2)
    g.add_edge(9, 0, 1)
    g.add_edge(1, 5, 25)
    g.add_edge(1, 4, 3)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 1.5)
    g.add_edge(3, 2, 0.5)
    g.add_edge(7, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(5, 7, 4)
    g.add_edge(8, 5, 3)
    g.add_edge(2, 1, 5)
    g.add_edge(7, 8, 2.5)
    g.add_edge(5, 9, 1.5)
    return g


def graph_creator_b():
    g = DiGraph()
    for i in range(9):
        g.add_node(i)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 3, 1)
    g.add_edge(4, 0, 1)

    g.add_edge(5, 8, 1)
    g.add_edge(7, 5, 1)
    g.add_edge(8, 7, 1)
    g.add_edge(8, 6, 1)
    return g


class TestGraphAlgo(unittest.TestCase):

    def test_load_and_save(self):
        g = graph_creator()
        graph = GraphAlgo()
        graph.__init__(g)
        self.assertTrue(graph.save_to_json("test_save"))
        self.assertTrue(graph.load_from_json("test_save"))
        load_graph = graph.get_graph()
        self.assertEqual(g, load_graph)
        g.remove_node(5)
        self.assertFalse(g, load_graph)

    def test_shortest_path_1(self):
        g = graph_creator()
        graph = GraphAlgo()
        graph.__init__(g)
        x1, y1 = graph.shortest_path(9, 9)
        x2, y2 = graph.shortest_path(9, 5)
        g.add_edge(1, 5, 1)
        x3, y3 = graph.shortest_path(9, 5)
        g.remove_edge(7, 6)
        x4, y4 = graph.shortest_path(4, 6)
        self.assertEqual(0, x1)
        self.assertEqual(6, x2)
        self.assertEqual(3, x3)
        self.assertEqual(-1, x4)

    def test_shortest_path_2(self):
        g = graph_creator()
        graph = GraphAlgo()
        graph.__init__(g)
        x, y = graph.shortest_path(2, 2)  # vertex to his self
        lst = [2]
        self.assertEqual(y == lst)
        lst.clear()
        x, y = graph.shortest_path(0, 6)  # node 0 to node 6
        lst = [0, 8, 5, 7, 6]
        self.assertTrue(y == lst)
        lst.clear()
        g.add_edge(1, 5, 1)
        x, y = graph.shortest_path(0, 6)  # find better path after changing weight in edge
        lst = [0, 1, 5, 7, 6]
        self.assertTrue(y == lst)
        lst.clear()
        g.remove_edge(7, 6)
        x, y = graph.shortest_path(0, 6)  # no path exist
        self.assertIsNone(y)

    def test_connected_components(self):
        g = graph_creator()
        graph = GraphAlgo()
        graph.__init__(g)
        lst = graph.connected_components()
        x0 = lst.pop(0)
        self.assertTrue([2, 3, 4] == x0)
        self.assertFalse([1, 2, 5] == x0)
        x1 = lst.pop(1)
        self.assertTrue([] == x1)
        x2 = lst.pop(2)
        self.assertTrue([3, 4, 0] == x2)
        x3 = lst.pop(3)
        self.assertTrue([0, 2, 4] == x3)
        x4 = lst.pop(4)
        self.assertTrue([0, 2, 3] == x4)
        x5 = lst.pop(5)
        self.assertTrue([7, 8] == x5)
        x6 = lst.pop(6)
        self.assertTrue([] == x6)
        x7 = lst.pop(7)
        self.assertTrue([8, 5] == x7)
        x8 = lst.pop(8)
        self.assertTrue([5, 7] == x8)


if __name__ == '__main__':
    unittest.main()
