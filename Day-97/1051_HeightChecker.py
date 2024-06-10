class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hn=sorted(heights)
        ans=0

        for i in range(len(heights)): 
            if hn[i]!= heights[i]: 
                ans+=1

        return ans
