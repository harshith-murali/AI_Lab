print("Harshith M : 1BM24CS113")

def cost(state):
    n = len(state)
    attacks = 0

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1

    return attacks


def hill_climbing(state):
    n = len(state)
    step = 0

    while True:
        current_cost = cost(state)
        print(f"\nStep {step}")
        print("Current State:", state)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("Goal reached!")
            return state

        best_state = state[:]
        best_cost = current_cost

        for i in range(n):
            for j in range(i + 1, n):
                neighbor = state[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

                neighbor_cost = cost(neighbor)
                print(f"Swap ({i},{j}): {neighbor}, Cost = {neighbor_cost}")

                if neighbor_cost < best_cost:
                    best_cost = neighbor_cost
                    best_state = neighbor

        if best_cost >= current_cost:
            print("Local minimum reached!")
            return state

        state = best_state
        step += 1


n = int(input("Enter number of queens: "))
state = list(map(int, input("Enter initial state: ").split()))

if n < 1 or len(state) != n or sorted(state) != list(range(n)):
    print("Enter a permutation of row numbers from 0 to n-1.")
else:
    result = hill_climbing(state)
    print("\nFinal State:", result)
    print("Final Cost:", cost(result))
