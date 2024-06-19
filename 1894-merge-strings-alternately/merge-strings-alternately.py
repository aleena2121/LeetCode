class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a = len(word1)
        b = len(word2)
        res = ""*(a+b)
        m = min(a,b)
        for i in range(m):
            res+=word1[i]
            res+=word2[i]
        if len(word1)==m:
            for j in range(m,len(word2)):
                res+=word2[j]
        else:
            for j in range(m,len(word1)):
                res+=word1[j]
        return res
        