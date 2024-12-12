import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            max_pile = max(gifts)
            gifts[gifts.index(max_pile)] = int(math.sqrt(max_pile))
        return sum(gifts)
