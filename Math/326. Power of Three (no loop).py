class Solution(object):
    def isPowerOfThree(self, n):
        # 3**19 = 1162261467 is an int, 3*20 is not an int
        return n > 0 and 1162261467 % n == 0

        """
        :type n: int
        :rtype: bool
        """