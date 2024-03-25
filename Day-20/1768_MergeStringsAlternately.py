class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        ans=[]
        leni=len(word1)
        lenj=len(word2)
        while i < leni and j <lenj:
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
        ans.append(word1[i:])
        ans.append(word2[j:])
        
        return "".join(ans)
