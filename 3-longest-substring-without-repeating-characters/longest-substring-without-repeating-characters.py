class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        if len(s)== 0:
            return 0
        for j in range(0,len(s)):
            res = []
            for i in range(j,len(s)):
                if s[i] not in res:
                    res.append(s[i])
                else:
                    break
            a.append(len(res))
        return max(a)
