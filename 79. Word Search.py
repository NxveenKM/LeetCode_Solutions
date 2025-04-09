class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'  # Mark the cell as visited

            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))

            board[r][c] = temp  # Restore the cell

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:  # Start searching from the first letter
                    if backtrack(r, c, 0):
                        return True

        return False
