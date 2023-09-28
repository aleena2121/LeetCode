class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e = []
        o = []
        for i in nums:
            if (i%2 == 0):
                e.append(i)
            else:
                o.append(i)
        for i in o:
            e.append(i)
        return e