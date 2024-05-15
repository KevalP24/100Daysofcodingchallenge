class Solution:
    def check(self, dist_nearest_thief, sf, n, directions):
        que = deque()

        visited = [[False for _ in range(n)] for _ in range(n)]
        que.append((0, 0))
        visited[0][0] = True

        if dist_nearest_thief[0][0] < sf:
            return False

        while que:
            curr_i, curr_j = que.popleft()

            if curr_i == n-1 and curr_j == n-1:
                return True

            for dir in directions:
                new_i = curr_i + dir[0]
                new_j = curr_j + dir[1]

                if 0 <= new_i < n and 0 <= new_j < n and not visited[new_i][new_j]:
                    if dist_nearest_thief[new_i][new_j] < sf:
                        continue
                    que.append((new_i, new_j))
                    visited[new_i][new_j] = True

        return False
    
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        dist_nearest_thief = [[-1 for _ in range(n)] for _ in range(n)]
        que = deque()
        visited = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    que.append((i, j))
                    visited[i][j] = True

        level = 0
        while que:
            size = len(que)

            for _ in range(size):
                curr_i, curr_j = que.popleft()
                dist_nearest_thief[curr_i][curr_j] = level
                for dir in directions:
                    new_i = curr_i + dir[0]
                    new_j = curr_j + dir[1]

                    if not (0 <= new_i < n and 0 <= new_j < n) or visited[new_i][new_j]:
                        continue

                    que.append((new_i, new_j))
                    visited[new_i][new_j] = True

            level += 1

        l, r = 0, 400
        result = 0

        while l <= r:
            mid_sf = l + (r - l) // 2

            if self.check(dist_nearest_thief, mid_sf, n, directions):
                result = mid_sf
                l = mid_sf + 1
            else:
                r = mid_sf - 1

        return result
