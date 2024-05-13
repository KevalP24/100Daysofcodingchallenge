class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        score = 2**(n - 1) * m

        for j in range(1, n):
            countSameBits = 0  
            for i in range(m):
                if grid[i][j] == grid[i][0]:
                    countSameBits += 1

            countOnes = countSameBits
            countZeros = m - countOnes

            ones = max(countOnes, countZeros)
            score += 2**(n - j - 1) * ones
        return score
