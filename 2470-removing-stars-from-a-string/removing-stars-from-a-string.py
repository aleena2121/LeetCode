class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            if i!="*":
                res.append(i)
            else:
                res.pop()
        return r''.join(res)