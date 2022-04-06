class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def maxValue(self, depth, state, a, b):
        legalActions = state.getLegalActions(0)
        if (
                depth > self.depth) or state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        maxEval = -9999999

        for action in legalActions:
            child = state.getNextState(0, action)
            maxEval = max(maxEval, self.minValue(depth, child, 1, a, b))
            if maxEval > b:
                return maxEval
            a = max(a, maxEval)
        return maxEval

    def minValue(self, depth, state, agentIndex, a, b):
        legalActions = state.getLegalActions(agentIndex)
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        minEval = 9999999

        agentCount = state.getNumAgents()
        if agentIndex <= agentCount - 2:
            for action in legalActions:
                child = state.getNextState(agentIndex, action)
                minEval = min(minEval, self.minValue(depth, child, agentIndex + 1, a, b))
                if minEval < a:
                    return minEval
                b = min(b, minEval)
        else:  # If there are no more ghosts after this one then it is pacman's (max) turn
            for action in legalActions:  # find the min value of pacman actions after the ghost takes each available action
                child = state.getNextState(agentIndex, action)
                minEval = min(minEval, self.maxValue(depth + 1, child, a, b))
                if minEval < a:
                    return minEval
                b = min(b, minEval)

        return minEval

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        bestActionValue = -9999999
        bestAction = None
        a = -9999999
        b = 9999999
        for action in gameState.getLegalActions(0):
            childState = gameState.getNextState(0, action)
            if self.minValue(1, childState, 1, a, b) > bestActionValue:
                bestActionValue = self.minValue(1, childState, 1, a, b)
                bestAction = action
            if bestActionValue > b:
                return bestAction
            a = max(a, bestActionValue)
        return bestAction