class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        count = 0
        for i in range (0,len(nums)):
            arr.append(nums.count(nums[i]))
        max_freq = max(arr)
        for i in nums:
            if nums.count(i)==max_freq:
                count+=1
        
        return count