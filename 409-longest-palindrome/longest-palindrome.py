class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        a = set(s)
        print(a)
        for i in a:
            if s.count(i)>1:
                res+=(s.count(i)//2)*2
                
        if len(s)==res:
            return res
        return res+1