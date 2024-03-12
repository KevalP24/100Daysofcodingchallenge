LEETCODE SOLUTION:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

FULL CODE:
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

def main():
    nums = [1, 2, 3]
    solution = Solution()
    concatenated_nums = solution.getConcatenation(nums)
    print(concatenated_nums)

if __name__ == "__main__":
    main()
