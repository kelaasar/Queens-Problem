def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_queens(board, col):
    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1

            if solve_queens(board, col + 1):
                return True

            board[row][col] = 0

    return False


board = [[0 for _ in range(8)] for _ in range(8)]

solve_queens(board, 0)

for row in board:
    print(row)


