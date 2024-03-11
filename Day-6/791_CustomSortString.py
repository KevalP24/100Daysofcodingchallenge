from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=''
        counter = Counter(s)
        for i in order:
            ans += i*counter[i]
            counter[i]=0
        for key,values in counter.items():
            ans += key*values
        return ans
