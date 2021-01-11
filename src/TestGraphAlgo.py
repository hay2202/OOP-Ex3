import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time


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
        # g = GraphAlgo()
        # g.load_from_json("/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_no_pos/G_10_80_0.json")
        # g.connected_components()
        g = GraphAlgo()
        g.load_from_json("/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_no_pos/G_1000_8000_0.json")
        start = time.time()
        g.connected_components()
        end = time.time()
        print("connected_components -> : %start sec" % (end - start))

    # graph.load_from_json("/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_on_circle/G_10_80_1.json")
    # graph.load_from_json("/Users/danielsela/PycharmProjects/OOP-Ex3/Graphs_random_pos/G_10_80_2.json")
    # graph.plot_graph()
    # print(graph.get_graph())
    # self.assertTrue(graph.save_to_json("test_save.json"))
    # self.assertTrue(graph.load_from_json("test_save.json"))
    # load_graph = graph.get_graph()
    # self.assertEqual(g, load_graph)
    # g.remove_node(5)
    # self.assertNotEqual(g, load_graph)

    def test_shortest_path_1(self):
        """
        find the shortest path between:
         1. vertex to his self.
         2. node 9 to node 5
         3. find better path after changing weight in edge
         4. no path exist.
        """
        g = graph_creator()
        graph = GraphAlgo(g)
        x1, y1 = graph.shortest_path(9, 9)  # 1
        x2, y2 = graph.shortest_path(9, 5)  # 2
        g.remove_edge(1, 5)
        g.add_edge(1, 5, 1)
        x3, y3 = graph.shortest_path(9, 5)  # 3
        g.remove_edge(7, 6)
        x4, y4 = graph.shortest_path(4, 6)  # 4
        self.assertEqual(0, x1)
        self.assertEqual(6, x2)
        self.assertEqual(3, x3)
        self.assertEqual(-1, x4)

    def test_shortest_path_2(self):
        g = graph_creator()
        graph = GraphAlgo(g)
        x, y = graph.shortest_path(2, 2)  # vertex to his self
        lst = [2]
        self.assertEqual(y, lst)
        lst.clear()
        x, y = graph.shortest_path(0, 6)  # node 0 to node 6
        lst = [0, 8, 5, 7, 6]
        self.assertTrue(y == lst)
        lst.clear()
        g.remove_edge(1, 5)
        g.add_edge(1, 5, 1)
        x, y = graph.shortest_path(0, 6)  # find better path after changing weight in edge
        lst = [0, 1, 5, 7, 6]
        self.assertTrue(y == lst)
        lst.clear()
        g.remove_edge(7, 6)
        x, y = graph.shortest_path(0, 6)  # no path exist
        self.assertIsNone(y)

    def test_connected_components(self):
        # graph = GraphAlgo()
        # graph.load_from_json("/Users/danielsela/PycharmProjects/OOP-Ex3/data/A1")
        # lst = graph.connected_component(1)
        # print(lst)
        g = graph_creator_b()
        graph = GraphAlgo(g)
        lst = graph.connected_components()
        x0 = lst.pop(0)
        self.assertTrue([0, 2, 3, 4] == x0)
        self.assertFalse([1, 2, 5] == x0)
        x1 = lst.pop(0)
        self.assertTrue([1] == x1)
        x2 = lst.pop(0)
        self.assertTrue([5, 7, 8] == x2)
        x2 = lst.pop(0)
        self.assertTrue([6] == x2)

    def test_draw_graph(self):
        g = GraphAlgo()
        g.load_from_json("/Users/danielsela/PycharmProjects/OOP-Ex3/data/A5")
        print(g.get_graph())
        g.plot_graph()


if __name__ == '__main__':
    unittest.main()
