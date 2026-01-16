class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for i in nums_set:
            if i+1 in nums_set:
                max_len = max(max_len, nums.count(i) + nums.count(i+1))
        return max_len