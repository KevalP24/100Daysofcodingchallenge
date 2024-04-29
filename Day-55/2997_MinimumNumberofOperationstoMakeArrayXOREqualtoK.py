class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        totalxor = 0
        
        for i in nums:
            totalxor ^= i
        
        diff =(totalxor ^ k)
        return bin(diff).count('1')
