class Solution:
    def dfs(self, nums, idx, mp):
        if idx == len(nums):
            self.result += 1
            return

        self.dfs(nums, idx + 1, mp)

        if not mp.get(nums[idx] - self.K, 0) and not mp.get(nums[idx] + self.K, 0):
            mp[nums[idx]] = mp.get(nums[idx], 0) + 1
            self.dfs(nums, idx + 1, mp)
            mp[nums[idx]] -= 1

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.result = 0
        self.K = k

        mp = {}

        self.dfs(nums, 0, mp)

        return self.result - 1
        
