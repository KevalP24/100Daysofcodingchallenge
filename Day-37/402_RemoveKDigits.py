class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []  
        n = len(num)
        for i in range(n):
            while ans and ans[-1] > num[i] and k > 0:
                ans.pop()
                k -= 1
            if ans or num[i] != '0':
                ans.append(num[i]) 
        
        while ans and k > 0:
            ans.pop()
            k -= 1
        
        if not ans:
            return "0"
        return ''.join(ans)
