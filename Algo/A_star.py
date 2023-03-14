import heapq

def heuristic(a, b):
    """
    A heuristic function that returns the Manhattan distance between two points a and b.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, target):
    """
    An implementation of A* search algorithm on a given grid with start and target positions.
    Returns a list of positions representing the path from start to target.

    :param grid: a Grid object representing the environment
    :param start: a tuple representing the starting position
    :param target: a tuple representing the target position
    :return: a list of positions representing the path from start to target
    """

    # Calculate the heuristic value of start to target distance
    h = heuristic(start, target)

    # Initialize the frontier and visited set
    frontier, moves = [], []
    heapq.heappush(frontier, (0, (start, moves)))
    visited = {start: 0}

    while frontier:
        _, cur = heapq.heappop(frontier)
        curPos, move = cur

        # If current position is target position, return the path
        if curPos == target:
            return move

        # Explore the successors of current position
        successors = grid.neighbors(curPos)
        for next_State in successors:
            # Calculate the cost of reaching the next state
            next_cost = visited[curPos]+1

            # If next state has not been visited or has been visited with higher cost, add it to the frontier
            if next_State not in visited or visited[next_State] > next_cost:
                visited[next_State] = next_cost
                temp = move.copy()
                temp.append(next_State)
                f = next_cost + heuristic(next_State, target)
                heapq.heappush(frontier, (f, (next_State, temp)))

    # If the frontier is empty but target position not reached, return an empty path
    return []
