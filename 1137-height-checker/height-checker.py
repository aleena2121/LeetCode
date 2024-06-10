class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        expected = sorted(heights)
        for i in range(0,len(heights)):
            if expected[i]!=heights[i]:
                res+=1
        return res