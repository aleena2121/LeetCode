class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        res1 = []
        res2 = []
        for i in range(0,len(s)):
            if (s[i]!='#'):
                res1.append(s[i])
            elif res1:
                res1.pop()
        for i in range(0,len(t)):
            if (t[i]!='#'):
                res2.append(t[i])
            elif res2:
                res2.pop()
                        
        if res1 == res2:
            return True
        else:
            return False