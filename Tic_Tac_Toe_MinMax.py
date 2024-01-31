import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, player):
    while True:
        row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
            break
        else:
            print("Cell already occupied. Try again.")

def minimax(board, depth, maximizing_player):
    if check_winner(board):
        return -1 if maximizing_player else 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def computer_move(board, computer):
    print(f"Computer ({computer}) is making a move...")
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = computer
                score = minimax(board, 0, False)
                board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = computer

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    computer = 'O'

    while True:
        print_board(board)

        if player == 'X':
            player_move(board, player)
        else:
            computer_move(board, computer)

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!" if player == 'X' else "Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
