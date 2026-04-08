from collections import deque

# Capacities of jugs
JUG1 = 4
JUG2 = 3
GOAL = 2

def get_next_states(x, y):
    states = []

    # Fill jug1
    states.append((JUG1, y))

    # Fill jug2
    states.append((x, JUG2))

    # Empty jug1
    states.append((0, y))

    # Empty jug2
    states.append((x, 0))

    # Pour jug1 -> jug2
    transfer = min(x, JUG2 - y)
    states.append((x - transfer, y + transfer))

    # Pour jug2 -> jug1
    transfer = min(y, JUG1 - x)
    states.append((x + transfer, y - transfer))

    return states

def bfs():
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Goal check
        if x == GOAL:
            return path

        for next_state in get_next_states(x, y):
            if next_state not in visited:
                queue.append((next_state, path))

    return None

# Run the solution
solution = bfs()

print("Steps to reach the goal:\n")
for step in solution:
    print(step)
