class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a=0
        b=0
        for i in s:
            a += ord(i)
        for i in t:
            b += ord(i)
        if b>a:
            c = b-a
            return chr(c)
        else:
            c = a-b
            return chr(c)