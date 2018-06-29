import numpy as np
import math


class Graph:

    def __init__(self, adjacency=None):
        self.adjacency = np.zeros((0, 0))
        self.nodes = []

    def distance_between(self, node1, node2):
        start = self.nodes[node1]
        end = self.nodes[node2]
        math.sqrt(math.pow(start.x - end.x, 2) + math.pow(start.y - end.y, 2))

    def heuristic_cost_approximate(self, node, goal):
        start = self.nodes[node]
        end = self.nodes[goal]
        math.sqrt(math.pow(start.x - end.x, 2) + math.pow(start.y - end.y, 2))

    def nodesUpdate(self, newNode):
        self.nodes.append(newNode)
        n = self.adjacency.shape[0]
        newAdjacency = np.zeros((n + 1, n + 1))
        newAdjacency[:-1, :-1] = self.adjacency
        self.adjacency = newAdjacency






