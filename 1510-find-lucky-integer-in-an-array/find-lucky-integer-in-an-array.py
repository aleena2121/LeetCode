class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ar = set(arr)
        ans = -1
        for i in ar:
            if arr.count(i)==i:
                ans = max(ans,i)
        return ans