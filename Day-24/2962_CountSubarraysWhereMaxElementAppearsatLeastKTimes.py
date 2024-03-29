class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle = max(nums)
        n = len(nums)
        i = 0
        j = 0
        ans = 0
        countMax = 0
        
        while j < n:
            if nums[j] == maxEle:
                countMax += 1
                
            while countMax >= k:
                ans += n - j
                
                if nums[i] == maxEle:
                    countMax -= 1
                i += 1
                
            j += 1
        
        return ans
