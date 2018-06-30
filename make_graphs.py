import pygame

from game.Game import Game
from graphs.Graph import Graph
from graphs.Node import Node
from search import A_star

pathGame = Game(10)
pathGame.choosingStart = False


def draw(game):
    game.gameDisplay.fill((255, 255, 255))
    for node in game.graph.nodes:
        pygame.draw.circle(game.gameDisplay, node.color, node.pos, game.node_radius)

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
        if game.choosingStart:
            node.isStart = False
        elif game.choosingGoal:
            node.isGoal = False
        if rectNode.contains(rectMouse):
            nowNode = node
            return nowNode

    nowNode = Node(mousePos)
    nowNode.num = len(game.graph.nodes)
    game.graph.nodesUpdate(nowNode)

    return nowNode
def update(g):
    game = g
    draw(game)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            chosenNode = check(pos, game)
            if game.currentNode is not None:
                game.graph.adjacency[game.currentNode.num, chosenNode.num] = 1
                game.graph.adjacency[chosenNode.num, game.currentNode.num] = 1
            if game.choosingStart:
                chosenNode.isStart = True
            elif game.choosingGoal:
                chosenNode.isGoal = True

            game.currentNode = chosenNode

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                game.currentNode = None
            elif event.key == pygame.K_c:
                return Game(10)
            elif event.key == pygame.K_s:
                game.choosingStart = True
            elif event.key == pygame.K_g:
                game.choosingGoal = True
            elif event.key == pygame.K_RETURN:

                game.findingPath = True
                game.graph = A_star(game.graph, update, game, 0.8)

        elif event.type == pygame.KEYUP:
            game.choosingStart = False
            game.choosingGoal = False

    pygame.display.update()
    pathGame.clock.tick(60)
    return game

while pathGame.running:
    pathGame = update(pathGame)
