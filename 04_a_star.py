def aStarSearch(problem, heuristic=nullHeuristic):
    frontier = util.PriorityQueue();
    expanded = []
    initial_state = problem.getStartState()
    frontier.push((initial_state,[],0 ),0)

    while(not frontier.isEmpty()):
        popped_element = frontier.pop()
        current_state,actions,total_cost = popped_element

        if current_state not in expanded:
            expanded.append(current_state)

            if(problem.isGoalState(current_state)):
                return actions
            for successors in problem.expand(current_state):
                next_pos, next_action, next_cost = successors
                new_cost = total_cost + next_cost
                f = new_cost + heuristic(next_pos,problem)
                frontier.push((next_pos,actions + [next_action], new_cost),f)

    util.raiseNotDefined()