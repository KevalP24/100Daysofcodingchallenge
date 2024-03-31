class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minPosi = -1
        maxPosi = -1
        outBound = -1
        for i in range(len(nums)):
            
            if nums[i] < minK or nums[i] > maxK:
                outBound = i
            if nums[i] == minK:
                minPosi = i
            if nums[i] == maxK:
                maxPosi = i
            
            count = min(maxPosi, minPosi) - outBound
            ans += count if count > 0 else 0
        
        return ans
