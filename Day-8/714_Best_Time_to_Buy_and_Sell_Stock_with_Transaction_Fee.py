class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit=0
        temp=prices[0]+fee
        for i in prices:
            if temp<i:
                profit+= i - temp
                temp = i
            elif i + fee < temp:
                temp = i + fee
        return profit
