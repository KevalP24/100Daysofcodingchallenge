class Solution:
    def solve(self, i, score, words, currScore, freq):
        self.maxScore = max(self.maxScore, currScore)
        
        if i >= self.n:
            return
        
        tempFreq = freq[:]
        
        j = 0
        tempScore = 0
        
        while j < len(words[i]):
            ch = words[i][j]
            tempFreq[ord(ch) - ord('a')] -= 1
            tempScore += score[ord(ch) - ord('a')]
            
            if tempFreq[ord(ch) - ord('a')] < 0:
                break
            
            j += 1
        
        if j == len(words[i]):
            self.solve(i + 1, score, words, currScore + tempScore, tempFreq)
        
        self.solve(i + 1, score, words, currScore, freq)
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = [0] * 26
        
        for ch in letters:
            freq[ord(ch) - ord('a')] += 1
        
        self.maxScore = float('-inf')
        self.n = len(words)
        
        self.solve(0, score, words, 0, freq)
        
        return self.maxScore
