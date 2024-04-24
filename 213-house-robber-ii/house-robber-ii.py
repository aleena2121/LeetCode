class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        r1,r2,a1,a2 = 0,0,0,0
        for n in range(0,len(nums)-1):
            temp = max(nums[n]+r1,r2)
            r1 = r2
            r2 = temp
        for n in range(1,len(nums)):
            temp1 = max(nums[n]+a1,a2)
            a1 = a2
            a2 = temp1
        return max(r2,a2)