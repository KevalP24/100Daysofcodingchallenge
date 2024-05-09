class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        tsum = 0
        t = 0

        for i in range(k):
            tsum += max(happiness[i] - t, 0)
            t += 1

        return tsum
