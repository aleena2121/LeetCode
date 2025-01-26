class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0

        if n & k != k:
            return -1

        while n>0:
            n1 = n & 1
            n2 = k & 1
            if n1 != n2:
                res+=1
            n = n>>1
            k = k>>1
        
        return res
        

