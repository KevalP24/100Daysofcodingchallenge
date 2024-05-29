class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s) 
        op = 0
        carry = 0
        
        for i in range(n-1,0, -1):
            if ((int(s[i]) + carry) % 2 ==0):  
                op += 1
            else:
                op +=2
                carry = 1
        
        return op + carry
