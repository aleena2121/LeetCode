from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = defaultdict(int)
        res = 0

        for row in grid:
            count[tuple(row)] += 1
        
        for col in zip(*grid):  
            if col in count:
                res += count[col]  

        return res