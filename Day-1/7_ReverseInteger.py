LEETCODE SOLUTION:
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

FULL CODE:
class Solution:
    def reverse(self, x: int) -> int:
        total = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            remainder = x % 10
            total = total * 10 + remainder
            x = x // 10
        if not -2**31 < total < 2**31:
            return 0
        return sign * total

def main():
    x = 123
    solution = Solution()
    reversed_x = solution.reverse(x)
    print("Reverse of", x, "is", reversed_x)

if __name__ == "__main__":
    main()
