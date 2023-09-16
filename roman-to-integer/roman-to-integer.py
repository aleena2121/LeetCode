class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        prev = None  

        for i in range(len(s)):
            if s[i] == "M":
                if prev == "C":
                    res += 800  
                else:
                    res += 1000
            elif s[i] == "D":
                if prev == "C":
                    res += 300 
                else:
                    res += 500
            elif s[i] == "C":
                if prev == "X":
                    res += 80 
                else:
                    res += 100
            elif s[i] == "L":
                if prev == "X":
                    res += 30  
                else:
                    res += 50
            elif s[i] == "X":
                if prev == "I":
                    res += 8 
                else:
                    res += 10
            elif s[i] == "V":
                if prev == "I":
                    res += 3 
                else:
                    res += 5
            elif s[i] == "I":
                res += 1
            
            prev = s[i]

        return res

                