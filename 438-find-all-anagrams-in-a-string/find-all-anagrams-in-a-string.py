from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        indices = []
        for left in range(len(s) - len(p) + 1):
            if Counter(s[left:left + len(p)]) == count_p:
                indices.append(left)
        return indices