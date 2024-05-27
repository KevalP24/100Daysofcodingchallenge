class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        ans = 0
        sett =set()
 
        for i in nums:
            if i in sett: 
                ans^= i
            else: 
                sett.add(i)  

        return ans
