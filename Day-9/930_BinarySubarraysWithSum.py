class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mp = {}
        count = 0
        curr_sum = 0
        mp[0] = 1
        for i in nums:
            curr_sum += i
            if curr_sum - goal in mp:
                count += mp[curr_sum - goal]
            if curr_sum in mp:
                mp[curr_sum] += 1
            else:
                mp[curr_sum] = 1
        return count
