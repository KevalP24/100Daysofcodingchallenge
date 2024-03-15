class Solution:
    def climbStairs(self, n: int) -> int:
        a,b,c=0,1,0
        for i in range(n):
            c=a+b
            a,b=b,c
        return b


DP SOLUTION:
class Solution:
    def helper(self,n,dp):
        if n<=1:
            return 1
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.helper(n-1,dp) + self.helper(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        return self.helper(n,dp)
