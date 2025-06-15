class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in nums:
            nums_set.add(int(str(i)[::-1]))
        return len(nums_set)