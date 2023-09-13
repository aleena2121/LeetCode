class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range (0,len(nums)):
            c = nums.count (nums[i])
            if (c==1):
                s = nums[i]
                break
        return s