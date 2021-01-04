from typing import List

import GraphInterface
import queue
import json
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from node import Node


def dijkstra(g, src, dest):
    q = queue.PriorityQueue()
    q.put(src)
    path = {src: -1}                    # adding the src to the path and queue
    while not q.empty():
        curr = g.get_node(q.get())
        if curr.info is None:           # true if we didn't visit this node
            curr.info = 'v'
            if curr.key == dest:        # when we get to dest node
                return path
            for k, v in g.all_out_edges_of_node(curr.key).items():       # moving on each neighbour of curr
                temp = g.get_node(k)
                if temp.info is None:       # true if we didn't visit this node
                    w = v
                    w += curr.weight
                    if temp.weight != 0:
                        if w < temp.weight:     # if the new weight is less then the exist
                            temp.weight = w
                            path[k] = curr.key
                    else:                        # if it's first time we reach to this node
                        temp.weight = w
                        path[k] = curr.key
                    q.put(temp.key)

    return path


def reset(g):
    map1 = g.get_all_v()
    for i in map1.keys():
        n = g.get_node(i)
        n.weight = 0.0
        n.tag = 0
        n.info = None


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        @return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        load_graph = DiGraph()
        try:
            with open(file_name, 'r') as f:
                dict_algo = json.load(f)
                nodes = dict_algo["nodes"]
                for k, v in nodes.items():
                    n = Node(**v)
                    load_graph.add_node(n.key, n.pos)
                edges = dict_algo["edges"]
                for k, v in edges.items():
                    for i in v.keys():
                        load_graph.add_edge(int(k), int(i), float(v.get(i)))
            self.graph = load_graph
        except IOError as e:
            print(e)
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, 'w') as fp:
                json.dump(self.graph, default=lambda m: m.__dict__, fp=fp, indent=4)
        except IOError as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        """
        if self.graph.get_node(id1) is None and self.graph.get_node(id2) is None:
            return -1, None
        if id1 == id2:
            return 0, [id1]
        reset(self.graph)
        path = dijkstra(self.graph, id1, id2)
        n = self.graph.get_node(id2)
        if n.weight == 0:               # true only if we didn't visit dest node
            return -1, None
        ans = []
        v = id2
        while v != -1:
            ans.append(v)
            v = path.get(v)
        ans.reverse()
        return n.weight, ans

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        raise NotImplementedError

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        raise NotImplementedError

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
