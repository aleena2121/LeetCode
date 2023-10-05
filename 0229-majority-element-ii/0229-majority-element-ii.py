class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums) 
        res = []
        for i in s:
            c = nums.count(i)
            if (c>(len(nums)/3)):
                res.append(i)
        
        return res