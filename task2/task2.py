import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing, depth):
    if check_winner("O"):
        return 10 - depth
    if check_winner("X"):
        return depth - 10
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, depth + 1)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, depth + 1)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, 0)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
        print("AI chooses position:", best_move + 1)

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("That position is already occupied. Try again.")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    print("=== TIC-TAC-TOE ===")
    print("You are X | AI is O")
    print("Choose a position from 1 to 9:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        human_move()
        print_board()

        if check_winner("X"):
            print("Congratulations! You win!")
            break

        if is_draw():
            print("It's a draw!")
            break

        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins! Better luck next time.")
            break

        if is_draw():
            print("It's a draw!")
            break

    print("Game over!")

play_game()