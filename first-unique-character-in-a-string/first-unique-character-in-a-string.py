class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        
        for e in s:
            if freq[e] == 1:
                return s.index(e)
            
        return -1