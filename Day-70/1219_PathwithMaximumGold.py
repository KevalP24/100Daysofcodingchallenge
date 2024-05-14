class Solution:
    def DFS(self, grid, i, j, directions):
        m, n = len(grid), len(grid[0])
        if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0:
            return 0  

        originalGoldValue = grid[i][j]
        grid[i][j] = 0
        maxGold = 0

        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            maxGold = max(maxGold, self.DFS(grid, new_i, new_j, directions))

        grid[i][j] = originalGoldValue
        return originalGoldValue + maxGold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxGold = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.DFS(grid, i, j, directions))

        return maxGold
