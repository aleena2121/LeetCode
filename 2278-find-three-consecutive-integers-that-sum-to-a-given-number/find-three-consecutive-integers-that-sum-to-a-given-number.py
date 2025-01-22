class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        x = num/3
        if (x-1)+x+(x+1)==num:
            res.append(x-1)
            res.append(x)
            res.append(x+1)
        return res