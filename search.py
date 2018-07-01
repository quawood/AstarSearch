from graphs.Graph import distance_between


def a_star(g, update, game, alpha=0.5, ):
    graph = g
    graph.set_neighbors()
    closedSet = []  # set of previously visited nodes

    startNode = [node for node in graph.nodes if node.isStart][0]
    openSet = [startNode]  # set of nodes that have been discovered but not visited

    startNode.fValue = graph.heuristic_cost_approximate(startNode)
    startNode.gValue = 0
    while not openSet == []:

        current = min(openSet, key=lambda x: x.fValue)

        if current.isGoal:
            current.isSolution = True
            atStart = False
            while not atStart:
                if current.isStart:
                    atStart = True
                else:
                    current.cameFrom.isSolution = True
                    current = current.cameFrom
            return graph

        openSet.remove(current)
        current.inOpen = False
        closedSet.append(current)
        current.inClosed = True

        for neighbor in current.neighbors:
            if neighbor in closedSet:
                continue

            if neighbor not in openSet:
                openSet.append(neighbor)
                neighbor.inOpen = True

            tentative_gValue = current.gValue + distance_between(current, neighbor)
            if tentative_gValue >= neighbor.gValue:
                continue

            neighbor.cameFrom = current
            neighbor.gValue = tentative_gValue

            # weight g and h cost based on alpha value
            neighbor.fValue = (1 - alpha) * neighbor.gValue + alpha * graph.heuristic_cost_approximate(neighbor)
        game.graph = graph
        update(game)
