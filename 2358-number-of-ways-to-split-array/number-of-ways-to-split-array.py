class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        Sum=sum(nums)
        acc, cnt=0, 0
        for i in range(n-1):
            acc+=nums[i]
            cnt+=(2*acc>=Sum)
        return cnt