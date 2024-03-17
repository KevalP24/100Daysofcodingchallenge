class Solution(object):
    def sumOfEncryptedInt(self, nums):

        def encrypt(num):
            maxnum = max(int(digit) for digit in str(num))
            encrypted = int(str(maxnum) * len(str(num)))
            return encrypted   
        tsum = 0
        for i in nums:
            tsum += encrypt(i)
        return tsum
