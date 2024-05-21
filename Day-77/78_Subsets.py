class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            ans += [curr + [i] for curr in ans]
        return ans
