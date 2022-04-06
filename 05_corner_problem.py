class CornersProblem(search.SearchProblem):

    def __init__(self, startingGameState):

        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print('Warning: no food in corner ' + str(corner))
        self._expanded = 0 # DO NOT CHANGE; Number of search nodes expanded

    def getStartState(self):
        state = (self.startingPosition, (0, 1, 2, 3))
        return state
        util.raiseNotDefined()

    def isGoalState(self, state):
        return not state[1]
        util.raiseNotDefined()

    def expand(self, state):
        children = []
        for action in self.getActions(state):
            x, y = state[0]
            dx, dy = Actions.directionToVector(action)
            nextX, nextY = int(x + dx), int(y + dy)

            if not self.walls[nextX][nextY]:
                remainedCorners = state[1] #lista cu colturile ramase
                nextLocation = (nextX, nextY)
                try:
                    idx = self.corners.index(nextLocation)
                except:
                    pass
                else:
                    if idx in remainedCorners:
                        temp = list(remainedCorners)
                        temp.remove(idx) #stergem colturile gasite
                        remainedCorners = tuple(temp)

                nextState = (nextLocation, remainedCorners)
                children.append((nextState, action, 1))
        self._expanded += 1 
        return children

    def getActions(self, state):
        possible_directions = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]
        valid_actions_from_state = []
        for action in possible_directions:
            x, y = state[0]
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]: 
                valid_actions_from_state.append(action)
        return valid_actions_from_state

    def getActionCost(self, state, action, next_state):
        assert next_state == self.getNextState(state, action), (
            "Invalid next state passed to getActionCost().")
        return 1 

    def getNextState(self, state, action):
        assert action in self.getActions(state), (
            "Invalid action passed to getActionCost().")
        x, y = state[0]
        dx, dy = Actions.directionToVector(action)
        nextx, nexty = int(x + dx), int(y + dy)

        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):

        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)