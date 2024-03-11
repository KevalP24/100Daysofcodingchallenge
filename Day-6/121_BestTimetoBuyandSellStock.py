# Approach-1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp , maxp = float('inf') , 0
        for i in prices:
            if i < minp:
                minp=i
            elif i-minp>maxp:
                maxp=i-minp
        return maxp


# approach-2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l,r=0,1
        # maxp=0
        # while r<len(prices):
        #     if prices[l]<prices[r]:
        #         currprofit=prices[r]-prices[l]
        #         maxp=max(currprofit,maxp)
        #     else:
        #         l=r
        #     r=r+1
        # return maxp
