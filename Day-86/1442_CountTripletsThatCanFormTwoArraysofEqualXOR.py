class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixXor = arr[:]
        triplets = 0        
        prefixXor.insert(0, 0)  
        n = len(prefixXor)
        
        for i in range(1, n):
            prefixXor[i] ^= prefixXor[i-1]

        for i in range(n):
            for k in range(i+1, n):
                if prefixXor[k] == prefixXor[i]:
                    triplets += k - i - 1
        
        return triplets
