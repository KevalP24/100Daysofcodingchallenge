class Solution:
    def countEven(self, num: int) -> int:
        n=0
        for i in range(1,num+1):
            sum=0
            while(i>0):
                k=i%10
                sum=sum+k
                i=i//10
            if sum%2==0:
                n+=1
        return n
