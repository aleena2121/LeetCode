class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 0
        if n == 1:
            return 1
        while (2**i) <= n:
            i += 1
        return (2**i) - 1