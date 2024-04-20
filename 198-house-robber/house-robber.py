class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1,r2 = 0,0
        for n in nums:
            temp = max(n+r1,r2)
            r1 = r2
            r2 = temp

        return r2
