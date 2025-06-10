from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        s_count = Counter(s)
        odd = []
        even = []
        for i in s_count.values():
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return max((max(odd)-min(even)),(min(odd)-max(even)))