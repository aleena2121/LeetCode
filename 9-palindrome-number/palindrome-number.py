class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z = str(x)
        y = z[::-1]
        return z==y