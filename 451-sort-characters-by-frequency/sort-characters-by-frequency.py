class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ""
        r = []
        res = ""
        for i in range(0,len(s)):
            if s[i] not in a:
                a+=s[i]
                r.append(s.count(s[i]))

        while(sum(r)!=0):
            d = max(r)
            c = r.index(d)
            r[c]=0
            res+=a[c]*d
        return res