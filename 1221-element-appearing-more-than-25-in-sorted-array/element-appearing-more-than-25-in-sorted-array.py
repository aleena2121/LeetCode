import math
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        x = math.floor(0.25*n)
        arr1 = set(arr)

        for i in arr1:
            count = 0
            for j in arr:
                if j==i:
                    count+=1
                if (count > x):
                    return j