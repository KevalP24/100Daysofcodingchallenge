class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        t = [0] * 26
        result = 0
        
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            left = max(0, curr - k)
            right = min(25, curr + k)

            longe = 0
            for j in range(left, right + 1):
                longe = max(longe, t[j])
            
            t[curr] = max(t[curr], longe + 1)
            result = max(result, t[curr])
        
        return result
