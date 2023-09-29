class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        increasing = decreasing = True  

        for k in range(len(nums) - 1):
            if nums[k] > nums[k + 1]:
                increasing = False
            elif nums[k] < nums[k + 1]:
                decreasing = False

        return increasing or decreasing