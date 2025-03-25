class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                # All queens are placed successfully
                board = []
                for i in range(n):
                    board.append("".join(['Q' if j == col[i] else '.' for j in range(n)]))
                result.append(board)
                return
            
            for c in range(n):
                if c in cols or (row - c) in diag1 or (row + c) in diag2:
                    continue  # Skip if the column or diagonals are under attack
                
                # Place the queen
                cols.add(c)
                diag1.add(row - c)
                diag2.add(row + c)
                col[row] = c  # Mark the column for the current row
                
                # Recur to place the next queen
                backtrack(row + 1)
                
                # Backtrack: remove the queen and mark the column and diagonals as free
                cols.remove(c)
                diag1.remove(row - c)
                diag2.remove(row + c)
        
        result = []
        cols = set()  # Columns where queens are placed
        diag1 = set()  # Diagonal (row - col)
        diag2 = set()  # Diagonal (row + col)
        col = [-1] * n  # To store the column index of the queen in each row
        
        backtrack(0)  # Start placing queens from the first row
        return result
