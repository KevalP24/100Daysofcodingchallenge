class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        result = []
        indegree = [0] * n
        adj = {}
        
        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        
        que = deque()
        for i in range(n):
            if indegree[i] == 1:
                que.append(i)
        
        while n > 2:
            size = len(que)
            n -= size
            
            for _ in range(size):
                u = que.popleft()
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 1:
                        que.append(v)
        
        result.extend(que)
        return result
