class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            lsum=i*(i+1)/2
            rsum=n*(n+1)/2 - i*(i-1)/2
            if lsum==rsum:
                return i
        return -1
