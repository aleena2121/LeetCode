class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        res = []
        for i in s1:
            if (s1.count(i)==1) and (i not in s2):
                res.append(i)
        for i in s2:
            if (s2.count(i)==1) and (i not in s1):
                res.append(i)
        return res