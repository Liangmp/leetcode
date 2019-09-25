class Solution(object):
    def intersect(self, nums1, nums2):
        a = []
        for i in nums1:
            if i in nums2:
                nums2.pop(nums2.index(i))
                a.append(i)
        return a 
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """