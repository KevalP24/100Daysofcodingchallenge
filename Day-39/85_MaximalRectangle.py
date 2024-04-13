class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        maxArea = 0
        m = len(matrix)
        n = len(matrix[0])
        
        def MAH(heights, n):
            st = []
            i = 0
            maxArea = 0
            area = 0
            while i < n:
                if not st or heights[i] >= heights[st[-1]]:
                    st.append(i)
                    i += 1
                else:
                    index = st.pop()
                    if not st:
                        area = heights[index] * i
                    else:
                        area = heights[index] * (i - st[-1] - 1)
                    maxArea = max(maxArea, area)
            
            while st:
                index = st.pop()
                if not st:
                    area = heights[index] * i
                else:
                    area = heights[index] * (i - st[-1] - 1)
                maxArea = max(maxArea, area)
            
            return maxArea
        
        heights = [0] * n
        for col in range(n):
            heights[col] = 0 if matrix[0][col] == '0' else 1
        
        maxArea = MAH(heights, n)
        
        for row in range(1, m):
            for col in range(n):
                if matrix[row][col] == '0':
                    heights[col] = 0
                else:
                    heights[col] += 1
            
            maxArea = max(maxArea, MAH(heights, n))
        
        return maxArea
