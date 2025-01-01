class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_one = s.count("1")
        count_zero = 0
        res = 0
        maxscore = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                count_zero+=1
            else:
                count_one-=1
            res = count_zero + count_one
            maxscore = max(maxscore,res)
        
        return maxscore