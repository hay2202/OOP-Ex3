import unittest
from DiGraph import DiGraph


# graph creator of 10 nodes 12 edges.
def graph_creator():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 8, 2)
    g.add_edge(9, 0, 1)
    g.add_edge(1, 5, 2.5)
    g.add_edge(1, 4, 3)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 1.5)
    g.add_edge(3, 2, 0.5)
    g.add_edge(7, 6, 1)
    g.add_edge(6, 7, 1)
    g.add_edge(5, 7, 4)
    g.add_edge(8, 5, 3)
    return g


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        g = graph_creator()
        v = g.v_size()
        self.assertEqual(10, v)

    def test_e_size(self):
        g = graph_creator()
        self.assertEqual(12, g.e_size())

    def test_get_all_v(self):
        g = graph_creator()
        v = g.get_all_v()
        self.assertEqual(10, v.__len__())

    def test_all_in_edges_of_node(self):
        g = graph_creator()
        v = g.all_in_edges_of_node(4)
        self.assertEqual(2, v.__len__())

    def test_all_out_edges_of_node(self):
        g = graph_creator()
        v = g.all_out_edges_of_node(4)
        self.assertEqual(1, v.__len__())

    def test_add_edge(self):
        g = graph_creator()
        g.add_edge(1, 2, 3.2)       # add new edge
        g.add_edge(5, 5, 1)         # edge to itself SHOULD NOT add
        g.add_edge(8, 5, 1)         # exist edge
        self.assertEqual(13, g.e_size())

    def test_add_node(self):
        g = graph_creator()
        g.add_node(5)      # exist node
        g.add_node(10)
        g.add_node(12)      # add twice the same node
        g.add_node(12)
        self.assertEqual(12, g.v_size())

    def test_remove_node(self):
        g = graph_creator()
        g.remove_node(7)
        g.remove_node(7)
        g.remove_node(20)
        self.assertEqual(9, g.v_size())
        self.assertEqual(9, g.e_size())

    def test_remove_edge(self):
        g = graph_creator()
        g.remove_edge(0, 1)
        g.remove_edge(0, 1)
        g.remove_edge(0, 0)
        g.remove_edge(0, 8)
        g.remove_edge(7, 6)
        self.assertEqual(9, g.e_size())


if __name__ == '__main__':
    unittest.main()
