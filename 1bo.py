print("Enter the number of queens")
N = int(input())

# Initialize the board
board = [[0] * N for _ in range(N)]

# Sets to track attacked columns and diagonals
cols = set()
diag1 = set()  # diagonal with slope i - j
diag2 = set()  # diagonal with slope i + j

def solve(row):
    if row == N:
        return True
    for col in range(N):
        if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
            board[row][col] = 1
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            if solve(row + 1):
                return True
            # Backtrack
            board[row][col] = 0
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    return False

solve(0)
for row in board:
    print(row)
