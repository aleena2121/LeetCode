class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = list(s)
        y = []
        for i in range(len(x)):
            if x[i].isalnum():
                y.append(x[i].lower())
        
        z = y[::-1]
        z_str = ''.join(z)
        y_str = ''.join(y)
        
        return z_str == y_str