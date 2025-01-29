class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = 0
        for i in nums:
            if nums.count(i)>2:
                ans = 1
       
        if ans == 0:
            return True
        return False
            