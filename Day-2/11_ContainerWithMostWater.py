LEETCODE SOLUTION:
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

FULL CODE:
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        ans = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            ans = max(area, ans)

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans

def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    max_area = solution.maxArea(height)
    print("Max area:", max_area)

if __name__ == "__main__":
    main()
