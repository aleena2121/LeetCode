class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = float("inf")
        i = 0
        while i<(len(blocks)-k+1):
            count = min(count, blocks[i:i+k].count("W"))
            i+=1
        
        return count