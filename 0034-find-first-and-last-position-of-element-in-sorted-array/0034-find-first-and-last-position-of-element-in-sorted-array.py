class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = -1
        y = -1
        if not nums:
            return [-1,-1]
        for i in range (0,len(nums)):
            if nums[i]==target:
                x = i
                break
        for i in range (len(nums)-1,-1,-1):
            if nums[i]==target:
                y = i
                break
        return [x,y]