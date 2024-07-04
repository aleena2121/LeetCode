class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        s1 = s.split()
        for i in range(len(s1)-1,-1,-1):
            res+=s1[i]
            if i!=0:
                res+=" "

        return res