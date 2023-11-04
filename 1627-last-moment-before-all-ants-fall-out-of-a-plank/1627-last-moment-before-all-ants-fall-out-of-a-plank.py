class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        time = 0
        for pos in left:
            time = max(time, pos)
        for pos in right:
            time = max(time, n - pos)
        return time
