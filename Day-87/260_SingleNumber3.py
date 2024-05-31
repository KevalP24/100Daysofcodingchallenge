class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_r = 0
        groupa = 0
        groupb = 0
        for i in nums:
            xor_r ^= i
        mask = xor_r & -xor_r

        for num in nums:
            if num & mask:
                groupa ^= num
            else:
                groupb ^= num
        return [groupa, groupb]
