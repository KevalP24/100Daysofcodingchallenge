class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum_value = 0
        count =0
        minLoss = float('inf')
        
        for num in nums:
            if (num ^k) > num:
                count += 1
                sum_value += (num ^ k)
            else:
                sum_value += num
            
            minLoss = min(minLoss,abs(num -(num ^k)))
        
        if count % 2 == 0:
            return sum_value
        
        return sum_value - minLoss
