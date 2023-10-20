class Solution(object):
    def searchInsert(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        e=len(nums)-1
        while s<=e:
            m=s+(e-s)/2
            if t>nums[m]:
                s=m+1
            elif t<nums[m]:
                e=m-1
            else: return m
        return s