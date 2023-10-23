class Solution:
    def isPowerOfFour(self, n):
        for i in range(16):
            power = 4 ** i
            
            if power == n:
                return True
            
            if power > n:
                return False
        
        return False