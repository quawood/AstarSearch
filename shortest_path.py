import pygame
import numpy as np
from Graph import Graph
from Node import Node


pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

graph = Graph()
currentNode = None

node_radius = 15


def draw(canvas):
    canvas.fill((255, 255, 255))
    for node in graph.nodes:
        pygame.draw.circle(canvas, (24, 138, 242), node.pos, node_radius)

    rowN = 0
    if graph.adjacency is not None:
        for row in range(0, len(graph.adjacency)):
            for col in range(rowN, len(graph.adjacency[row])):
                if graph.adjacency[row, col] == 1:
                    pygame.draw.line(canvas, (0, 0, 0), graph.nodes[row].pos, graph.nodes[col].pos, 3)
                    pygame.draw.line

            rowN += 1


def check(mousePos):
    nowNode = None
    for node in graph.nodes:
        rectMouse = (mousePos[0], mousePos[1], 1, 1)
        rectNode = pygame.Rect((node.pos[0] - node_radius, node.pos[1] - node_radius),
                               (2 * node_radius, 2 * node_radius))
        if rectNode.contains(rectMouse):
            nowNode = node
            return nowNode

    nowNode = Node(mousePos)
    nowNode.num = len(graph.nodes)
    graph.nodesUpdate(nowNode)

    return nowNode

while running:
    draw(gameDisplay)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()

            chosenNode = check(mousePos)
            if currentNode is not None:
                graph.adjacency[currentNode.num, chosenNode.num] = 1
                graph.adjacency[chosenNode.num, currentNode.num] = 1

            currentNode = chosenNode

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                currentNode = None

    pygame.display.update()
    clock.tick(60)
