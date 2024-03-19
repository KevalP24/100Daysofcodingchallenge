class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # approach-1
        n=len(nums)
        real_sum= n*(n+1)//2
        curr_sum=sum(nums)
        return real_sum - curr_sum


        # approach-2
        #n=len(nums)
        #sum1=n*(n+1)//2
        #sum2=0
        #for i in nums:
        #    sum2 += i
        #return sum1-sum2
