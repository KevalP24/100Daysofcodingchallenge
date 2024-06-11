class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n-=1
        rounde = k//n
        rem=k%n

        if rounde%2==0:
            return rem
        else:
            return n-rem
