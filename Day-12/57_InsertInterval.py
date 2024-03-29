class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i=0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
        return ans
