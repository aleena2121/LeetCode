class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        nums = sorted(nums)
        if len(nums)>1:
            for i in range(0,len(nums)-1):
                res.append(abs(nums[i]-nums[i+1]))
            return max(res)
        return 0
