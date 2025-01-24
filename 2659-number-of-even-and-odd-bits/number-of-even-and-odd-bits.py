class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0,0]
        i = 0

        while n:
            ans[i] += n & 1
            n >>= 1
            i ^= 1
            
        return ans
        