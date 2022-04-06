def foodHeuristic(state, problem):
    position, foodGrid = state
    foods = foodGrid.asList()
    if not foods:
        return 0

    maxDistance = 0
    for food in foods:
        key = position + food
        if key in problem.heuristicInfo:
            distance = problem.heuristicInfo[key]
        else:
            distance = mazeDistance(position, food, problem.startingGameState)
            problem.heuristicInfo[key] = distance

        if distance > maxDistance:
            maxDistance = distance

    return maxDistance