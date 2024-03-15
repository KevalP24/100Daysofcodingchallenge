class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [0] * n
        s = [0] * n
        p[0] = 1
        s[n-1] = 1
        ans = [0] * n

        for i in range(1, n):
            p[i] = p[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            s[i] = s[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = p[i] * s[i]
        
        return ans
