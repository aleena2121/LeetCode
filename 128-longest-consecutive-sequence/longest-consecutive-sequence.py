class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0
        for i in numSet:
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                max_len = max(length, max_len)
        return max_len