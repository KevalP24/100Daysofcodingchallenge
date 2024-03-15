class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        tsum=sum(nums)
        for i in range(len(nums)):
            if lsum == tsum-lsum-nums[i]:
                return i
            lsum+=nums[i]
        return -1
