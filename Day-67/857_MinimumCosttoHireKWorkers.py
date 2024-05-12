class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        wage2Quality = [[wage[i]/quality[i], quality[i]] for i in range(n)]
        wage2Quality.sort()
        curTotalQuality = 0
        maxHeap = []

        for i in range(k):
            heapq.heappush(maxHeap, -wage2Quality[i][1])
            curTotalQuality += wage2Quality[i][1]
        
        ans = curTotalQuality * wage2Quality[k-1][0]
        
        for i in range(k, n):
            heapq.heappush(maxHeap, -wage2Quality[i][1])
            
            curTotalQuality += wage2Quality[i][1] + heapq.heappop(maxHeap)
            
            ans = min(ans, curTotalQuality * wage2Quality[i][0])
        
        return ans
