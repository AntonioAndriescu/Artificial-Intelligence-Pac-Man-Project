class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def maxValue(self, depth, state):
        actions = state.getLegalActions(0)
        if (depth > self.depth) or state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        maxEval = -9999999

        for action in actions:
            child = state.getNextState(0, action)
            maxEval = max(maxEval, self.minValue(depth, child, 1))
        return maxEval

    def minValue(self, depth, state, agentIndex):
        actions = state.getLegalActions(agentIndex)
        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        minEval = 9999999

        agentCount = state.getNumAgents()
        if agentIndex <= agentCount - 2:
            for action in actions:
                child = state.getNextState(agentIndex, action)
                minEval = min(minEval, self.minValue(depth, child, agentIndex + 1))
        else:
            for action in actions:
                child = state.getNextState(agentIndex, action)
                minEval = min(minEval, self.maxValue(depth + 1, child))

        return minEval

    def getAction(self, gameState):
        "*** YOUR CODE HERE ***"
        agent = 0

        bestActionValue = -9999999
        bestAction = None
        for action in gameState.getLegalActions(0):
            nextState = gameState.getNextState(0, action)
            if self.minValue(1, nextState, 1) > bestActionValue:
                bestActionValue = self.minValue(1, nextState, 1)
                bestAction = action
        return bestAction