class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        s1 = set(s)
        print(s1)
        odd = 0
        for i in s1:
            if s.count(i)%2 != 0:
                odd+=1
        print(odd)
        if odd > k:
            return False
        return True