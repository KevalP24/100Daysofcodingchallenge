
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)     
        mp = {}
        currSum = 0
        ans = 0
        mp[0] = -1
        for i in range(n):
            currSum += 1 if nums[i] == 1 else -1
            if currSum in mp:
                ans = max(ans, i - mp[currSum])
            else:
                mp[currSum] = i  
        return ans
