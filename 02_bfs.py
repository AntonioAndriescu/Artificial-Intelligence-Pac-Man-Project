def breadthFirstSearch(problem):
    frontier = util.Queue();
    expanded = []
    initial_state = problem.getStartState()
    frontier.push((initial_state, []))

    while (not frontier.isEmpty()):
        popped_element = frontier.pop()
        current_state, actions = popped_element

        if (current_state not in expanded):
            expanded.append(current_state)
            if (problem.isGoalState(current_state)):
                return actions
            for successor in problem.expand(current_state):
                next_pos, next_action, cost = successor
                frontier.push((next_pos, actions + [next_action]))
    util.raiseNotDefined()