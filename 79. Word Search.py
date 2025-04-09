class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        counter = Counter([board[x][y] for x in range(ROWS) for y in range(COLS)])

        counter_word = Counter(word)

        for char in counter_word:
            if counter.get(char, 0) < counter_word[char]:
                return False
        
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                board[r][c] == '#'):
                return False
            
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

#bute force lol
