class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack=[]
        cmin=nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack  and n>stack[-1][-1]:
                return True
            stack.append([n,cmin])
            cmin=min(cmin,n)
        return False 



