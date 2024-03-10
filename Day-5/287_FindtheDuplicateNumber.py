class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        values = set()
        for ele in nums:
            if ele in values:
               return ele
            values.add(ele)
