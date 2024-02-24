class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            a = [0] * (i + 1)  # Initialize the row with zeros
            a[0] = 1
            a[-1] = 1
            for j in range(1, len(a) - 1):
                a[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(a)
        return res