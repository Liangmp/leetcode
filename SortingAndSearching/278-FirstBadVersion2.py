# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        return self.recursive(1,n);
    
    def recursive(self, left, right):
        if left == right:
            return left
        else:
            mid = (left + right) // 2
            if isBadVersion(mid):
                return (self.recursive(left, mid))
            else:
                return (self.recursive(mid+1, right))
        """
        :type n: int
        :rtype: int
        """