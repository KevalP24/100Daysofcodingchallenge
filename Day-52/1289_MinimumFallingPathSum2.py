class Solution:
    def solve(self, row, col, grid, t):
        if row == self.n - 1:
            return grid[row][col]

        if t[row][col] != -1:
            return t[row][col]

        ans = float('inf')
        for nextCol in range(self.n):
            if nextCol != col:
                ans = min(ans, self.solve(row + 1, nextCol, grid, t))

        t[row][col] = grid[row][col] + ans
        return t[row][col]

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        t = [[-1] * self.n for _ in range(self.n)]

        result = float('inf')
        for col in range(self.n):
            result = min(result, self.solve(0, col, grid, t))

        return result
        
