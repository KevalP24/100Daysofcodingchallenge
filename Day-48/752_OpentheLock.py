class Solution:
    def fill_neighbors(self, queue, curr, dead):
        for i in range(4):
            ch = curr[i]
            dec = chr(ord(ch) - 1) if ch != '0' else '9'
            inc = chr(ord(ch) + 1) if ch != '9' else '0'
            curr_list = list(curr)

            curr_list[i] = dec
            new_curr = ''.join(curr_list)
            if new_curr not in dead:
                dead.add(new_curr)
                queue.append(new_curr)

            curr_list[i] = inc
            new_curr = ''.join(curr_list)
            if new_curr not in dead:
                dead.add(new_curr)
                queue.append(new_curr)

    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1
        queue = deque()
        queue.append(start)
        level = 0
        
        while queue:
            n = len(queue)

            for _ in range(n):
                curr = queue.popleft()
                if curr == target:
                    return level
                self.fill_neighbors(queue, curr, dead)
            level += 1
        return -1
