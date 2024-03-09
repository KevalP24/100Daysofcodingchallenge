class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        ans=0
        while i<j:
            area = (j-i) * min(height[i],height[j])
            ans=max(area,ans)

            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return ans
