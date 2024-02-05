class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        for i in range(0,len(s)):
            x = s.count(s[i])
            if x==1:
                return i
                break

        return -1