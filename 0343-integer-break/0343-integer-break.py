class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        elif n==3:
            return 2

        elif n%3==0:
            return pow(3,n//3)
        elif n%3==1:
            return 4*pow(3,(n-4)//3)
        else:
            return 2*pow(3,(n-2)//3)