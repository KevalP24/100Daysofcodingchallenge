class Solution:
    def makeGood(self, s: str) -> str:
        ans = ""
        
        for ch in s:
            if ans and (ord(ch) + 32 == ord(ans[-1]) or ord(ch) - 32 == ord(ans[-1])):
                ans = ans[:-1]  
            else:
                ans += ch
        
        return ans
