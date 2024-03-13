class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        for i in range (0,n):
            sum1 = sum(arr[:i])
            sum2 = sum(arr[i + 1:])
            if sum1 == sum2:
                return arr[i]
        
    
        return -1