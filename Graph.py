import numpy as np

class Graph:


    def __init__(self, adjacency):
        self.adjacency = adjacency
        self.n_nodes = adjacency.shape[0]

        self.f_values = np.zeros(self.n_nodes)  # total estimated cost of being at node n
        self.g_values = np.zeros(self.n_nodes)  # cost of going from start node to n
        self.h_values = np.zeros(self.n_nodes)  # estimates cost of cheapest path from n to target node

