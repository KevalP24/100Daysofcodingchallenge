class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n=len(s)
        weremove = set()
        stack = []     
        ans = ""
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    weremove.add(i)
                else:
                    stack.pop()
        
        while stack:
            weremove.add(stack.pop())
    
        for i in range(n):
            if i not in weremove:
                ans += s[i]
        return ans
