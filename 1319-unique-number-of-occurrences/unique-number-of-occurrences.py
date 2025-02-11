class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        res = []
        for i,j in freq.items():
            if j not in res:
                res.append(j)
            else:
                return False
        return True        