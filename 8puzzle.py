import heapq

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

MOVES = {
    "Up": -3,
    "Down": 3,
    "Left": -1,
    "Right": 1
}

def manhattan_distance(state):
    """Calculate Manhattan Distance heuristic"""
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = GOAL_STATE.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):
    """Generate valid neighbor states"""
    neighbors = []
    zero_index = state.index(0)

    row, col = divmod(zero_index, 3)

    for move, position_change in MOVES.items():
        new_index = zero_index + position_change

        if move == "Up" and row == 0:
            continue
        if move == "Down" and row == 2:
            continue
        if move == "Left" and col == 0:
            continue
        if move == "Right" and col == 2:
            continue

        new_state = list(state)
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        neighbors.append((tuple(new_state), move))

    return neighbors


def solve_puzzle(initial_state):
    """Solve 8 puzzle using A* search"""

    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state))

    came_from = {}
    g_cost = {initial_state: 0}

    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)

        if current_state == GOAL_STATE:
            return reconstruct_path(came_from, current_state)

        for neighbor, move in get_neighbors(current_state):
            tentative_g = g_cost[current_state] + 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + manhattan_distance(neighbor)
                heapq.heappush(priority_queue, (f_cost, neighbor))
                came_from[neighbor] = (current_state, move)

    return None


def reconstruct_path(came_from, current):
    """Reconstruct solution path"""
    path = []
    while current in came_from:
        current, move = came_from[current]
        path.append(move)
    path.reverse()
    return path


def print_state(state):
    """Print puzzle in 3x3 format"""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


if __name__ == "__main__":
    
    initial_state = (1, 2, 3,
                     4, 0, 6,
                     7, 5, 8)

    print("Initial State:")
    print_state(initial_state)

    solution = solve_puzzle(initial_state)

    if solution:
        print("Solution found!")
        print("Moves:", solution)
        print("Number of moves:", len(solution))
    else:
        print("No solution exists.")