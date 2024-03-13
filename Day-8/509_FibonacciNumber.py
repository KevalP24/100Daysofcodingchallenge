LEETCODE SOLUTION:
class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        ans=0
        if n<2:
            return n
        else:
            for i in range(2,n+1):
                ans=a+b
                a=b
                b=ans    
        return ans
