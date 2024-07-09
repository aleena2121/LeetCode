class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        res = []
        currtime = 0
        for i in customers:
            arrival = i[0]
            time = i[1]
            while arrival>currtime:
                currtime+=1
            currtime += time
            res.append(currtime - arrival)
        
        return sum(res)/float(len(res))