    def evaluationFunction(self, currentGameState, action):
        
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        if childGameState.isWin():
            return 9999999

        closestFood = min([manhattanDistance(newPos, food) for food in newFood.asList()])

        for ghost in newGhostStates:
            if ghost.scaredTimer == 0 and manhattanDistance(ghost.getPosition(), newPos) < 2:
                return -9999999

        return childGameState.getScore() + 1 / closestFood