class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l =len(nums)

        for i in range (0,l,2):
            nums[i] ,nums[i+1] = nums[i+1] ,nums[i]

        
        return nums
