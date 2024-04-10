class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        ind =deque(range(n))
        idx=0
        for i in deck:
            idx = ind.popleft()  
            ans[idx] = i     
            if ind:              
                ind.append(ind.popleft())  
        
        return ans
