# 8-Puzzle using Iterative Deepening Search (IDS)

def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
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


def depth_limited_search(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(
                neighbor,
                goal,
                depth - 1,
                path + [neighbor]
            )

            if result:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        print("Searching at depth:", depth)

        result = depth_limited_search(
            start,
            goal,
            depth,
            [start]
        )

        if result:
            return result

        depth += 1


start = tuple(map(int, input(
    "Enter initial state (use 0 for blank): ").split()))

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

print("\nInitial State:")
display(start)

solution = ids(start, goal)

print("Solution found using IDS:")

for state in solution:
    display(state)