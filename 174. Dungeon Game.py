class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0
        
        rows, cols = len(dungeon), len(dungeon[0])
        # Create a DP table with the same dimensions as the dungeon
        dp = [[0] * cols for _ in range(rows)]
        
        # Start from the bottom-right corner
        dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])
        
        # Fill the last row
        for j in range(cols - 2, -1, -1):
            dp[rows - 1][j] = max(1, dp[rows - 1][j + 1] - dungeon[rows - 1][j])
        
        # Fill the last column
        for i in range(rows - 2, -1, -1):
            dp[i][cols - 1] = max(1, dp[i + 1][cols - 1] - dungeon[i][cols - 1])
        
        # Fill the rest of the DP table
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        # The answer is the minimum health required at the starting position
        return dp[0][0]
