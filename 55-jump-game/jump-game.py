class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = 0
        for i in nums:
            if ans<0:
                return False
            elif i>ans:
                ans = i
            ans-=1
        return True       