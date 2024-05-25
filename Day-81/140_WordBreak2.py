class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        tmp, res = [], [] 

        def dfs(i):
            if i == n:
                res.append(" ".join(tmp))
            for j in range(i, n):
                if s[i:j+1] in wordSet:
                    tmp.append(s[i:j+1])
                    dfs(j+1)
                    tmp.pop()
        dfs(0)
        return res
