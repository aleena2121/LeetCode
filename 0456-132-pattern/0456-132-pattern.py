class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        stack = []
        s3 = float("-inf")

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True

            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()

            stack.append(nums[i])

        return False