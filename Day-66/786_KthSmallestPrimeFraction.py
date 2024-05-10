class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        pq = []

        for i in range(n):
            heapq.heappush(pq, (arr[i] / arr[-1], i, n - 1))

        smallest = 1

        while smallest < k:
            frac, i, j = heapq.heappop(pq)
            j -= 1

            if j > i:
                heapq.heappush(pq, (arr[i] / arr[j], i, j))
            
            smallest += 1

        frac, i, j = heapq.heappop(pq)
        return [arr[i], arr[j]]
