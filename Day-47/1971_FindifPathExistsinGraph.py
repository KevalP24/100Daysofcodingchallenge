class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    if dfs(i, visited):
                        return True
            return False
        
        visited = set()
        return dfs(source, visited)
