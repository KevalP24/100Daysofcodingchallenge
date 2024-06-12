class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) 
        n =len(citations)
        ans= 0

        for i in range(n):
            if citations[i]>=i+1: 
                ans =i+1
        
        return ans
