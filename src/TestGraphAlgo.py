import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def graph_creator():
    g = DiGraph()
    for i in range(5):
        g.add_node(i)
    g.add_edge(0, 4, 1)
    g.add_edge(0, 3, 2)
    g.add_edge(4, 3, 2)
    g.add_edge(3, 0, 5)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 1, 1)
    return g


class TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        g = graph_creator()
        g2=GraphAlgo()
        g2.__init__(g)
        self.assertEqual(g2,g)
        sad



    def test_load_and_save(self):

    def test_shortest_path(self):

    def test_connected_component(self):

    def test_connected_components(self):


if __name__ == '__main__':
    unittest.main()
