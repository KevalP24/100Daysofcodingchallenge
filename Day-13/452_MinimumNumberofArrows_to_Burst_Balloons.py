class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()        
        prev = points[0]
        count = 1

        for i in range(1, n):
            currStartPoint, currEndPoint = points[i]
            prevStartPoint, prevEndPoint = prev
            if currStartPoint > prevEndPoint:  
                count += 1
                prev = points[i]
            else:
                prev[0] = max(prevStartPoint, currStartPoint)
                prev[1] = min(prevEndPoint, currEndPoint)
        
        return count
