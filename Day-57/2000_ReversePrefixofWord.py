class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans=word.find(ch)

        if ans==-1: 
            return word
            
        res=list(word[:ans+1])
        res1=list(word[ans+1:])
        res.reverse()

        return "".join(res+res1)
