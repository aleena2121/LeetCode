class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1 = sorted(nums)
        for i in range(len(nums)):
            if nums1 == (nums[i:]+nums[:i]):
                return True
        return False