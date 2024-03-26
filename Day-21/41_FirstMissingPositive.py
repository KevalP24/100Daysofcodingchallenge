class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=set(nums)
        a=1
        while a in n:
            a+=1
        return a
        
    
