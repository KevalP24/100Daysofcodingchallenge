class Solution:
    def dfs(self, land, i, j, r2, c2):
        land[i][j] = 0
        r2[0] = max(r2[0], i)
        c2[0] = max(c2[0], j)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dir_ in directions:
            i_ = i + dir_[0]
            j_ = j + dir_[1]
            if 0 <= i_ < self.m and 0 <= j_ < self.n and land[i_][j_] == 1:
                self.dfs(land, i_, j_, r2, c2)
                
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.m = len(land)
        self.n = len(land[0])
        result = []
        for i in range(self.m):
            for j in range(self.n):
                if land[i][j] == 1:
                    r1, c1 = i, j
                    r2, c2 = [-1], [-1]
                    self.dfs(land, i, j, r2, c2)
                    result.append([r1, c1, r2[0], c2[0]])
        
        return result
