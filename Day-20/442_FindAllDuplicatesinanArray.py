class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            idx = abs(i)-1
            if nums[idx]<0:
                ans.append(abs(i))
            else:
                nums[idx] *= -1
        return ans
