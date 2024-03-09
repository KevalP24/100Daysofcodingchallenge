class Solution:
    def reverse(self, x: int) -> int:
        sum=0
        sign=1
        if x<0:
            sign=-1
            x=-x
        while x>0:
            r=x%10
            sum=sum*10+r
            x=x//10
        if not -2**31<sum<2**31:
            return 0
        return sign*sum
