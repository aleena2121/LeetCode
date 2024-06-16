class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            if nums.count(i)>2:
                if i!=10000:
                    for j in range(0,len(nums)):
                        if nums[j]==i:
                            nums[j]=10000
                            break
        nums.sort()
        for i in nums:
            if i!=10000:
                c+=1
        return c