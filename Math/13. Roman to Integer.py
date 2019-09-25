# This solution is from agave in Leetcode Discuss

class Solution(object):
    def romanToInt(self, s):
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result, previous = 0, "I"
        for char in s[::-1]:
            result, previous = result - d[char] if d[char] < d[previous] else result + d[char], char
        return result
    
        """
        :type s: str
        :rtype: int
        """  