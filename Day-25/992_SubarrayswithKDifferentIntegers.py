class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            mp = {}
            n = len(nums)
            i = 0
            count = 0

            for j in range(n):
                mp[nums[j]] = mp.get(nums[j], 0) + 1

                while len(mp) > k:
                    mp[nums[i]] -= 1
                    if mp[nums[i]] == 0:
                        del mp[nums[i]]
                    i += 1

                count += (j - i + 1)
            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)
