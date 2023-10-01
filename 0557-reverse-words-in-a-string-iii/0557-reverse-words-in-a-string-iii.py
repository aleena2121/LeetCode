class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        res = ""
        for i in s:
            if not i.isspace():
                r.append(i)
            else:
                while r:
                    res += r.pop()
                res += " "
    
        while r:
            res += r.pop()
        return res