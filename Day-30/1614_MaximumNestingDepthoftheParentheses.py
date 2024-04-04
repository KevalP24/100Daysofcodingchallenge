class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maxi = 0
        for i in s:
            if i=='(':
                counter+=1
            if i==')':
                maxi=max(counter,maxi)
                counter-=1
        return maxi
