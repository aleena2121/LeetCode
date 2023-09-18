class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        n = str(x)
        length = len(n)
        n = n[::-1]
        
        if n[-1] == "-":
            x = "-"
            s = n[0:length-1]
            n = x + s
        
        reversed_int = int(n)
        
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        return reversed_int