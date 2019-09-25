class Solution(object):
    def rotate(self, nums, k):
        nums[0:k], nums[k:len(nums)] = nums[len(nums)-k:len(nums)], nums[0:len(nums)-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        