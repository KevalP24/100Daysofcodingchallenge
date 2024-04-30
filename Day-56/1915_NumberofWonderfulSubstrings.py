class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = {0: 1}
        c_xor =0
        result= 0

        for i in word:
            shift = ord(i) - ord('a')
            c_xor ^= (1 << shift)
            result += mp.get(c_xor, 0)
            for j in range(ord('a'), ord('j') + 1):
                shift = j - ord('a')
                check_xor = c_xor ^ (1 << shift)
                result += mp.get(check_xor, 0)

            mp[c_xor] = mp.get(c_xor, 0) + 1

        return result
