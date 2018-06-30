import pygame

from game.Game import Game
from search import A_star

rows = 50
columns = 50
cell_radius = 7
pathGame = Game(rows, columns, cell_radius)


def draw(game):

    game.gameDisplay.fill((255, 255, 255))

    for dnode in game.graph.nodes:
        pygame.draw.circle(game.gameDisplay, dnode.color, dnode.pos,
                           game.node_radius, dnode.width)


def check(mousePos, game):
    if not game.findingPath:
        for node in pathGame.graph.nodes:
            left, top = node.x - game.node_radius, node.y - game.node_radius
            nodeRect = pygame.Rect((left, top), (2 * game.node_radius, 2 * game.node_radius))
            if mousePos.contains(nodeRect):
                if not (node.isStart or node.isGoal or node.isWall):
                    if game.choosingStart:
                        node.isStart = True
                        game.choosingStart = False
                        game.choosingGoal = True
                        return

                    elif game.choosingGoal:
                        node.isGoal = True
                        game.choosingGoal = False
                        game.creatingWalls = True
                        return

                    elif game.creatingWalls:
                        node.isWall = True


def update(g):
    game = g
    draw(game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.dragging = True
            pos = pygame.mouse.get_pos()
            frame_radius = game.node_radius + 5
            left, top = pos[0] - frame_radius, pos[1] - frame_radius
            mousePos = pygame.Rect(left, top, frame_radius * 2, frame_radius * 2)
            if game.creatingWalls:
                mousePos = pygame.Rect(left, top, 50, 50)
            check(mousePos, game)

        elif event.type == pygame.MOUSEMOTION:
            if game.dragging:
                pos = pygame.mouse.get_pos()
                frame_radius = game.node_radius + 5
                left, top = pos[0] - frame_radius, pos[1] - frame_radius
                mousePos = pygame.Rect(left, top, 50, 50)
                check(mousePos, game)
        elif event.type == pygame.MOUSEBUTTONUP:
            game.dragging = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game.creatingWalls:
                    for node in game.graph.nodes:
                        if node.isWall:
                            game.graph.adjacency[node.num, :] = 0
                            game.graph.adjacency[:, node.num] = 0

                    game.findingPath = True
                    game.graph = A_star(game.graph, update, game)
            elif event.key == pygame.K_c:
                return Game(rows, columns, cell_radius)
    pygame.display.update()
    game.clock.tick(60)

    return game

while pathGame.running:
    pathGame = update(pathGame)
