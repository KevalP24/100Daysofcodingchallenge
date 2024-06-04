class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        char_set = set()
        result = 0

        for ch in s:
            if ch in char_set:
                char_set.remove(ch)
                result += 2
            else:
                char_set.add(ch)
        
        if char_set:
            result += 1
        
        return result
