LEETCODE SOLUTION:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return -1

FULL CODE:
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1

def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution()
    index = solution.search(nums, target)
    print("Index of", target, "in", nums, ":", index)

if __name__ == "__main__":
    main()
