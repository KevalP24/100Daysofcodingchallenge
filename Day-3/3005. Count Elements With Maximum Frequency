class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = [0] * 101
        maxfreq,total = 0,0

        for i in nums:
            arr[i] += 1
            
            if arr[i] > maxfreq:
                maxfreq = arr[i]
                total = arr[i]
            elif arr[i] == maxfreq:
                total += arr[i]
        return total
