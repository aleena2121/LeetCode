class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        even = 0
        for i in nums:
            if i % 2 == 0:
                even += 1
            if even == 2:
                return True
                break
        return False
