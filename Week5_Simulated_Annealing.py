print("Harshith M : 1BM24CS113")

import random
import math


def cost(board):
    attacks = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1

    return attacks


def simulated_annealing(board, temp, alpha, min_temp):
    n = len(board)
    step = 0

    while temp > min_temp and cost(board) > 0:
        neighbor = board[:]

        col = random.randrange(n)
        new_row = random.choice(
            [r for r in range(n) if r != board[col]]
        )
        neighbor[col] = new_row

        old_cost = cost(board)
        new_cost = cost(neighbor)

        delta = new_cost - old_cost

        if delta < 0:
            accept = True
        else:
            probability = math.exp(-delta / temp)
            accept = random.random() < probability

        if accept:
            board = neighbor

        step += 1

        print(f"Step {step}: {board}, "
              f"Cost = {cost(board)}, "
              f"Temperature = {temp:.4f}")

        temp *= alpha

    return board


n = int(input("Enter number of queens: "))
board = list(map(int, input("Enter initial state: ").split()))
temp = float(input("Enter initial temperature: "))
alpha = float(input("Enter cooling factor: "))
min_temp = float(input("Enter minimum temperature: "))

if (n < 2 or len(board) != n
        or any(r < 0 or r >= n for r in board)
        or temp <= 0 or not 0 < alpha < 1
        or min_temp <= 0):
    print("Invalid input.")
else:
    result = simulated_annealing(board, temp, alpha, min_temp)

    print("\nFinal State:", result)
    print("Final Cost:", cost(result))

    if cost(result) == 0:
        print("Solution Found!")
    else:
        print("Stopped at minimum temperature.")
