import pygame

from game.Game import Game
from graphs.Node import Node
from search import a_star


pathGame = Game(10)
pathGame.choosingStart = False


def draw(game):
    game.gameDisplay.fill((255, 255, 255))

    rowN = 0
    if game.graph.adjacency is not None:
        for row in range(0, len(game.graph.adjacency)):
            for col in range(rowN, len(game.graph.adjacency[row])):
                if game.graph.adjacency[row, col] == 1:
                    color = (0, 0, 0)
                    if game.graph.nodes[row].isSolution and game.graph.nodes[col].isSolution:
                        color = (82, 239, 43)

                    pygame.draw.line(game.gameDisplay, color, game.graph.nodes[row].pos, game.graph.nodes[col].pos,
                                     3)

            rowN += 1

    for node in game.graph.nodes:
        pygame.draw.circle(game.gameDisplay, node.color, node.pos, game.node_radius)


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
        if event.type == pygame.QUIT:
            game.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            chosenNode = check(pos, game)

            if game.choosingStart:
                chosenNode.isStart = True
            elif game.choosingGoal:
                chosenNode.isGoal = True
            elif game.currentNode is not None and not game.currentNode == chosenNode:
                game.graph.adjacency[game.currentNode.num, chosenNode.num] = 1
                game.graph.adjacency[chosenNode.num, game.currentNode.num] = 1

            game.currentNode = chosenNode

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # d press
                game.currentNode = None
            elif event.key == pygame.K_s:  # s press
                game.choosingStart = True
            elif event.key == pygame.K_g:  # g press
                game.choosingGoal = True
            elif event.key == pygame.K_RETURN:  # enter press
                if game.graph.hasGoal and game.graph.hasStart:
                    game.findingPath = True  # start finding path
                    game.graph = a_star(game.graph, update, game, 0.8)
            elif event.key == pygame.K_c:  # c press
                return Game(10)  # clear graph

        elif event.type == pygame.KEYUP:
            game.choosingStart = False
            game.choosingGoal = False

    pygame.display.update()
    pathGame.clock.tick(60)
    return game

while pathGame.running:
    pathGame = update(pathGame)
