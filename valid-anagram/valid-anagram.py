class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = list(s)
        y = list(t)
        k = 0
        
        if (len(x)==len(y)):
            for i in t:
                if (i not in x):
                    k+=1
                else:
                    x.remove(i)
        else :
            k+=1
        if (k==0):
            return True
        else:
            return False