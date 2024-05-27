class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)

        for num in nums:
            freq[min(n, num)] += 1

        csum = 0

        for i in range(n, -1, -1):
            csum += freq[i]
            if i == csum:
                return i
        return -1
