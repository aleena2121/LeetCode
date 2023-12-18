class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        nums.remove(b)
        c = min(nums)
        nums.remove(c)
        d = min(nums)
        return (a*b)-(c*d)
