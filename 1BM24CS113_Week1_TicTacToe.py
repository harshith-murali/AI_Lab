# Tic-Tac-Toe Game

def display_board(board):
    print("\n")
    for i in range(3):
        print(" " + " | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False


def tic_tac_toe():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    player = "X"

    print("TIC-TAC-TOE")
    print("Player X and Player O")

    for turn in range(9):
        display_board(board)

        print("Player", player, "turn")
        choice = int(input("Enter position (1-9): ")) - 1

        if choice < 0 or choice > 8 or board[choice] in ["X", "O"]:
            print("Invalid move! Try again.")
            continue

        board[choice] = player

        if check_winner(board, player):
            display_board(board)
            print("Player", player, "wins!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    display_board(board)
    print("It's a draw!")


tic_tac_toe()