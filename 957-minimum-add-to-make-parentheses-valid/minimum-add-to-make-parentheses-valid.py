class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        o,c= 0,0
        for i in s:
            if i == '(':
                o+=1
            else:
                if o!=0:
                    o-=1
                else:
                    c+=1
        return (o+c)