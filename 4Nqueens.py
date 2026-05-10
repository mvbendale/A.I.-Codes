N = 6
board = [[0]*N for _ in range(N)]

cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)

def solve(row):
    if row == N:
        for r in board:
            print(r)
        print()
        return
        
    for col in range(N):
        if not cols[col] and not diag1[row - col + (N - 1)] and not diag2[row + col]:
      
            board[row][col] = 1
            cols[col] = True
            diag1[row - col + (N - 1)] = True
            diag2[row + col] = True
            
            # Recursion (Branching)
            solve(row + 1)
            
            # Backtrack
            board[row][col] = 0
            cols[col] = False
            diag1[row - col + (N - 1)] = False
            diag2[row + col] = False

solve(0)
