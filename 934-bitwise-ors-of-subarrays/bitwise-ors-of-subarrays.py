class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        cur = set()
        for i in arr:
            cur = {i|x for x in cur} | {i}
            res.update(cur)

        return len(res)