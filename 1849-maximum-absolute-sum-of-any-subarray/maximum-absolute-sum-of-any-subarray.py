class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1 = nums[0]
        res2 = nums[0]
        maxEnding = nums[0]
        minEnding = nums[0]

        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            res1 = max(res1, maxEnding)
            minEnding = min(minEnding + nums[i], nums[i])
            res2 = min(res2, minEnding)
        
        return max(res1, abs(res2)) 