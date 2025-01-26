class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n>0:
            x = n & 1
            if x == 1:
                res+=1
            n = n >> 1
        return res