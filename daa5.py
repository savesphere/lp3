
# 8-Queens Problem using Backtracking

N = 8

def print_board(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()


def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main Program
board = [[0] * N for _ in range(N)]

# Place first queen at (0, 0)
board[0][0] = 1

if solve_n_queens(board, 1):
    print("Final 8-Queens Matrix:")
    print_board(board)
else:
    print("No solution exists.")
