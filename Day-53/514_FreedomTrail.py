class Solution:
    def count_steps(self, ring_index, i, n):
        dist = abs(i - ring_index)
        wrap_around = n - dist
        return min(dist, wrap_around)

    def solve(self, ring_index, key_index, ring, key, t):
        if key_index == len(key):
            return 0
        
        if t[ring_index][key_index] != -1:
            return t[ring_index][key_index]
        
        result = float('inf')
        for i in range(len(ring)):
            if ring[i] == key[key_index]:
                total_steps = self.count_steps(ring_index, i, len(ring)) + 1 + \
                              self.solve(i, key_index + 1, ring, key, t)
                result = min(result, total_steps)
        
        t[ring_index][key_index] = result
        return result

    def findRotateSteps(self, ring: str, key: str) -> int:
        t = [[-1] * 101 for _ in range(101)]
        return self.solve(0, 0, ring, key, t)
