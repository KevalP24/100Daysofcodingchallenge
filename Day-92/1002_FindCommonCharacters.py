class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        n =len(words)
        count= [0]*26
        
        for ch in words[0]:
            count[ord(ch)- ord('a')] +=1

        for i in range(1, n):
            temp = [0]*26
            for ch in words[i]:
                temp[ord(ch) -ord('a')]+= 1
            for i in range(26):
                if count[i] != temp[i]:
                    count[i] = min(count[i], temp[i])
            
        for i in range(26):
            if count[i] != 0:
                c =count[i]
                while c> 0:
                    result.append(chr(i+ ord('a')))
                    c -=1
        
        return result
