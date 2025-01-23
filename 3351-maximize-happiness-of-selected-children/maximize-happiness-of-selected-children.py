class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()  
        sum = 0
        dec = 0
        index = len(happiness) - 1

        for i in range(0,k):
            if (happiness[index]-dec)>0:
                sum += happiness[index] - dec
                dec += 1
                index -= 1  
            else:
                break 
        return sum