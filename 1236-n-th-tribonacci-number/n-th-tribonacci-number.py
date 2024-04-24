class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        f = [0]*(n+1)
        f[0] = 0
        f[1] = f[2] = 1
        for i in range(3,n+1):
            f[i] =f[i-3] + f[i-2] + f[i-1]

        return f[n]