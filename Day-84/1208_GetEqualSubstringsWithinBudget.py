class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans = 0
        currCost = 0
        i = 0
        j = 0

        while j < n:
            currCost += abs(ord(s[j]) - ord(t[j]))
            
            while currCost > maxCost:
                currCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            
            ans = max(ans, j - i + 1)
            j += 1
        return ans
