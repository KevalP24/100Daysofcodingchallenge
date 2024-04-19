class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i,j)
                    self.dfs(grid,i,j)
                    ans+= 1
        return ans
 
    def dfs(self,grid,i,j):
        grid[i][j] = 0
        for dx,dy in (1,0), (-1,0), (0,-1), (0,1):
            r = i + dx
            c = j + dy
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)
