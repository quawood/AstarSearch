import numpy as np
import pygame

from graphs.Graph import Graph
from graphs.Node import Node


class Game:

    def __init__(self, rows, columns, node_radius):
        self.rows, self.cols = rows, columns
        self.node_radius = node_radius
        self.gameWidth, self.gameHeight = 2 * node_radius * columns, 2 * node_radius * rows

        self.graph = Graph()
        self.currentNode = None
        self.shortestPath = []
        self.findingPath = False

        self.choosingStart = True
        self.choosingGoal = False
        self.creatingWalls = False

        pygame.init()

        self.gameDisplay = pygame.display.set_mode((self.gameWidth, self.gameHeight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dragging = False

        self.create_nodes()

    # create nodes for graph in a grid
    def create_nodes(self):
        self.graph.adjacency = np.zeros((self.rows * self.cols, self.rows * self.cols))
        nNodes = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                position = tuple(2 * c * self.node_radius + self.node_radius for c in (col, row))
                node = Node(position)
                node.num = nNodes
                self.graph.nodes.append(node)

                nextRight = nNodes + 1  # the node to the right
                nextDown = nNodes + self.cols  # the node to the bottom
                nextDownRight = nextDown + 1
                nextDownLeft = nextDown - 1

                # if nodes exist either right or down, make the current node and that node neighbors
                if col < self.cols - 1:
                    self.graph.adjacency[nNodes, nextRight] = 1
                    self.graph.adjacency[nextRight, nNodes] = 1
                if row < self.rows - 1:
                    self.graph.adjacency[nNodes, nextDown] = 1
                    self.graph.adjacency[nextDown, nNodes] = 1
                if col < self.cols - 1 and row < self.rows - 1:
                    self.graph.adjacency[nNodes, nextDownRight] = 1
                    self.graph.adjacency[nextDownRight, nNodes] = 1
                if col > 0 and row < self.rows - 1:
                    self.graph.adjacency[nNodes, nextDownLeft] = 1
                    self.graph.adjacency[nextDownLeft, nNodes] = 1

                nNodes += 1
