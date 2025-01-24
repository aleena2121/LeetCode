class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarrays = []
        n = len(nums)
        num = set(nums)
        n1 = len(num)   
        count = 0     
        for start in range(n):
            num1 = set()
            for end in range(start, n):
                num1.add(nums[end])
                if len(num1) == n1 :
                    count += 1
        
        return count
        