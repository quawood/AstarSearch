import numpy as np
from Graph import Graph

def A_star():

    graph = Graph(np.array([]))


    start = 0
    goal = len(graph.nodes) - 1

    closedSet = []
    openSet = [start]
    gValues = [0]
    fValues = [graph.heuristic_cost_approximate(start, goal)]
    cameFrom = [None]

    while not openSet == []:
        index = fValues.index(min(fValues))
        current = index

        del openSet[openSet.index(current)]
        closedSet.append(index)

        connections = graph.adjacency[current]
        neighbors = [connections.index(neighbor) for neighbor in connections if neighbor > 0]

        for neighbor in neighbors:
            if neighbor in closedSet:
                continue

            if not neighbor in openSet:
                openSet.append(neighbor)

            tentative_gValue = gValues[current] + graph.distance_between(current, neighbor)
            if tentative_gValue >= gValues[neighbor]:
                continue

            cameFrom[neighbor] = current
            gValues[neighbor] = tentative_gValue
            fValues[neighbor] = gValues[neighbor] + graph.heuristic_cost_approximate(neighbor, goal)


