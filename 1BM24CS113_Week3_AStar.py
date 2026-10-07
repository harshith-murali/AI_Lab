# A* Algorithm for 8-Puzzle

import heapq


def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def manhattan_distance(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])

            row1 = i // 3
            col1 = i % 3

            row2 = goal_index // 3
            col2 = goal_index % 3

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start, goal):
    pq = []

    h = manhattan_distance(start, goal)

    # (f, g, state, path)
    heapq.heappush(pq, (h, 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:
                new_g = g + 1
                new_h = manhattan_distance(neighbor, goal)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Input
start = tuple(map(int, input(
    "Enter initial state (use 0 for blank): ").split()
))

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

print("\nInitial State:")
display(start)

solution = a_star(start, goal)

if solution:
    print("Solution using A*:\n")

    for state in solution:
        display(state)

    print("Number of moves:", len(solution) - 1)

else:
    print("No solution found.")