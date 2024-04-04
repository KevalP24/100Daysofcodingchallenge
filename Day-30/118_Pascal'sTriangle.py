class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==0:
            return []
        if numRows == 1:
            return [[1]]
            
        ans = self.generate(numRows - 1)
        temp = [1] * numRows
        
        for i in range(1, numRows - 1):
            temp[i] = ans[-1][i - 1] + ans[-1][i]
        
        ans.append(temp)
        return ans
