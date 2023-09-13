class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range (0,len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    res.extend([i,j])
                    
        return res
                    