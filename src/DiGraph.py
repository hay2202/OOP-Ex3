from GraphInterface import GraphInterface
from node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.in_edges = {}
        self.mc = 0
        self.num_of_nodes = 0
        self.num_of_edges = 0

    def v_size(self) -> int:
        return self.num_of_nodes

    def e_size(self) -> int:
        return self.num_of_edges

    def get_mc(self) -> int:
        return self.mc

    def get_all_v(self) -> dict:
        """ return a dictionary of all the nodes in the Graph,
         each node is represented using a pair  (key, node_data) """
        return self.nodes

    def get_node(self, id1):
        """
        :param id1:
        :return: return the node with given ID
        """
        if self.nodes.__contains__(id1):
            return self.nodes[id1]
        else:
            return None

    def all_in_edges_of_node(self, id1: int) -> dict:
        """ return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight) """

        return self.in_edges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """ return a dictionary of all the nodes connected from node_id ,
        each node is represented using a pair (key, weight) """

        return self.edges.get(id1)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        """

        if self.nodes.__contains__(id1) and self.nodes.__contains__(id2) and id1 != id2 and not self.has_edge(id1, id2):
            self.edges[id1][id2] = weight
            self.in_edges[id2][id1] = weight
            self.num_of_edges += 1
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        """

        if self.nodes.__contains__(node_id):
            return False
        self.nodes[node_id] = node.Node(node_id, pos)
        self.in_edges[node_id] = {}
        self.edges[node_id] = {}
        self.num_of_nodes += 1
        self.mc += 1

        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        """
        if self.nodes.__contains__(node_id):
            out = self.all_out_edges_of_node(node_id)
            for i in out:
                self.in_edges[i].pop(node_id)
            self.edges.pop(node_id)
            self.num_of_edges -= out.__len__()
            self.mc += out.__len__()

            inside = self.all_in_edges_of_node(node_id)
            for i in inside:
                self.edges[i].pop(node_id)
                self.num_of_edges -= 1
                self.mc += 1

            self.in_edges.pop(node_id)
            self.nodes.pop(node_id)
            self.num_of_nodes -= 1
            self.mc += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        """

        if self.has_edge(node_id1, node_id2):
            self.edges[node_id1].pop(node_id2)
            self.in_edges[node_id2].pop(node_id1)
            self.num_of_edges -= 1
            self.mc += 1
            return True
        return False

    def has_edge(self, id1, id2):
        if self.edges[id1].__contains__(id2):
            return True
        else:
            return False

    def __str__(self):
        return f"num of nodes: {self.num_of_nodes}, num of edges: {self.num_of_edges}, mc: {self.mc}," \
               f" nodes: {self.nodes}, edges: {self.edges}, in edges: {self.in_edges}"
