'''
This is a perfect coding challenge to explain XOR

For this problem, by XORing all the numbers in the vector, the only number left will be the non-repeated number. All other repeated numbers cancel themselves because n^n = 0.

Input [2,2,1]: 2^2^1 = 0^1 = 1
Input [4,1,2,1,2]: 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4

-- Explained by coder_cat in Leetcode

'''

class Solution(object):
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
        """
        :type nums: List[int]
        :rtype: int
        """