import pygame

from game.Game import Game
from graphs.Graph import Graph
from graphs.Node import Node
from search import A_star

pathGame = Game(50, 50, 10)


def draw(game):
    game.gameDisplay.fill((255, 255, 255))
    for node in game.graph.nodes:
        pygame.draw.circle(game.gameDisplay, (24, 138, 242), node.pos, game.node_radius)

    rowN = 0
    if game.graph.adjacency is not None:
        for row in range(0, len(game.graph.adjacency)):
            for col in range(rowN, len(game.graph.adjacency[row])):
                if game.graph.adjacency[row, col] == 1:
                    pygame.draw.line(game.gameDisplay, (0, 0, 0), game.graph.nodes[row].pos, game.graph.nodes[col].pos,
                                     3)

            rowN += 1


def check(mousePos, game):
    for node in game.graph.nodes:
        rectMouse = (mousePos[0], mousePos[1], 1, 1)
        rectNode = pygame.Rect((node.pos[0] - game.node_radius, node.pos[1] - game.node_radius),
                               (2 * game.node_radius, 2 * game.node_radius))
        if rectNode.contains(rectMouse):
            nowNode = node
            return nowNode

    nowNode = Node(mousePos)
    nowNode.num = len(game.graph.nodes)
    game.graph.nodesUpdate(nowNode)

    return nowNode

while pathGame.running:
    draw(pathGame)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            chosenNode = check(pos, pathGame)
            if pathGame.currentNode is not None:
                pathGame.graph.adjacency[pathGame.currentNode.num, chosenNode.num] = 1
                pathGame.graph.adjacency[chosenNode.num, pathGame.currentNode.num] = 1

            pathGame.currentNode = chosenNode

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pathGame.currentNode = None
            elif event.key == pygame.K_c:
                graph = Graph()
                pathGame.currentNode = None
            elif event.key == pygame.K_RETURN:

                A_star(graph, 0, len(graph.nodes) - 1)

    pygame.display.update()
    pathGame.clock.tick(60)
