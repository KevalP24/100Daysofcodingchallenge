class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n =len(nums)
        mp = defaultdict(int)
        sum= 0
        mp[0] = 1
        ans =0
        
        for i in range(n):
            sum += nums[i]
            rem = sum % k            
            if rem < 0:
                rem += k
            
            if rem in mp:
                ans += mp[rem]
            
            mp[rem] += 1        
        return ans
