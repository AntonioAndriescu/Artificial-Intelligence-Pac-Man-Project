def cornersHeuristic(state, problem):
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    position = state[0]
    cornersIndices = state[1]
    if not cornersIndices:
        return 0

    return max([util.manhattanDistance(position, corners[idx]) for idx in cornersIndices])