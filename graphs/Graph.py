import numpy as np
import math


class Graph:

    def __init__(self):
        self.adjacency = np.zeros((0, 0))
        self.nodes = []
        self.start = 0
        self.goal = 0

    def distance_between(self, node1, node2):
        return math.sqrt(math.pow(node1.x - node2.x, 2) + math.pow(node1.y - node2.y, 2))

    def heuristic_cost_approximate(self, node):
        goal = [node for node in self.nodes if node.isGoal][0]
        return math.sqrt(math.pow(node.x - goal.x, 2) + math.pow(node.y - goal.y, 2))

    def nodesUpdate(self, newNode):
        self.nodes.append(newNode)
        n = self.adjacency.shape[0]
        newAdjacency = np.zeros((n + 1, n + 1))
        newAdjacency[:-1, :-1] = self.adjacency
        self.adjacency = newAdjacency

    def set_neighbors(self):
        for node1 in self.nodes:
            for node2 in self.nodes:
                if self.adjacency[node1.num, node2.num] == 1:
                    node1.neighbors.append(node2)
