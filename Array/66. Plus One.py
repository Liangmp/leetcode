class Solution(object):
    def plusOne(self, digits):
        stringValue = ''
        for digit in digits:
            stringValue += str(digit)
        addOneValue = int(stringValue) + 1
        return list(str(addOneValue))
        """
        :type digits: List[int]
        :rtype: List[int]
        """