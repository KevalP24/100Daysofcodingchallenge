class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = {}
        i = 0
        j = 0
        ans = 0
        
        while j < n:
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            
            while i < j and mp[nums[j]] > k:
                mp[nums[i]] -= 1
                i += 1
                
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans
