class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = list(s.strip().split())
        return len(ans[-1])
