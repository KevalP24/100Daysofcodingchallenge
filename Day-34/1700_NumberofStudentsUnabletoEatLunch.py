class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        arr = [0, 0]

        for i in students:
            arr[i] += 1
        
        for j in range(n):
            if arr[sandwiches[j]] == 0:
                return n - j
            arr[sandwiches[j]] -= 1
        
        return 0
