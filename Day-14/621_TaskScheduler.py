class Solution:
    def leastInterval(self, tasks, p):
        n = len(tasks)
        if p == 0:
            return n        
        counter = [0] * 26

        for ch in tasks:
            counter[ord(ch) - ord('A')] += 1
        
        counter.sort()
        chunks = counter[-1] - 1
        idol = chunks * p
        
        for i in range(24, -1, -1):
            idol -= min(chunks, counter[i])
        if idol > 0:
            return n + idol
        return n
