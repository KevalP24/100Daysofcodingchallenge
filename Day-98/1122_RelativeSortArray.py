class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {num: i for i, num in enumerate(arr2)}
        large_value = float('inf')

        for num in arr1:
            if num not in mp:
                mp[num] = large_value

        def custom_sort(num1, num2):
            if mp[num1] == mp[num2]:
                return num1 - num2
            return mp[num1] - mp[num2]

        arr1.sort(key=lambda x: (mp[x], x))

        return arr1
