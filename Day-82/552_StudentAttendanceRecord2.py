class Solution:
    def solve(self, n, absent, consecutive_late, t, M):
        if absent >= 2 or consecutive_late >= 3:
            return 0

        if n == 0:
            return 1

        if t[n][absent][consecutive_late] != -1:
            return t[n][absent][consecutive_late]

        A = self.solve(n-1, absent+1, 0, t, M) % M
        L = self.solve(n-1, absent, consecutive_late+1, t, M) % M
        P = self.solve(n-1, absent, 0, t, M) % M

        t[n][absent][consecutive_late] = ((A + L) % M + P) % M
        return t[n][absent][consecutive_late]
    def checkRecord(self, n: int) -> int:
        M = 10**9 + 7
        t = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        return self.solve(n, 0, 0, t, M)
