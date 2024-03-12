class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            if nums[i]<k:
                ans+=1
        return ans
