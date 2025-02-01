class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        l = len(flowerbed)
        
        for i in range(l):
            if flowerbed[i]==0:

                left_empty = (i==0 or flowerbed[i-1]==0)
                right_empty = (i==l-1 or flowerbed[i+1]==0)

                if right_empty and left_empty:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt >= n:
                        return True

        return cnt>=n