class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[00]
        sum_so_far = 0
        for i in range(len(nums)):
            if sum_so_far < 0:
                sum_so_far = 0
            sum_so_far += nums[i]
            max_sum = max(sum_so_far, max_sum)
        return max_sum
            
