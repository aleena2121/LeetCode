class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        while numBottles>=numExchange:
            q = numBottles//numExchange 
            r = numBottles%numExchange
            numBottles = q + r      
            res += q

        return res