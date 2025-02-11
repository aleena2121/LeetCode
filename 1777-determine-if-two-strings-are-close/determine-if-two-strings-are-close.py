class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        s1 = sorted(set(word1))
        s2 = sorted(set(word2))
        if s1 != s2:
            return False
        l1 = []
        l2 = []
        for i in range(len(s1)):
            l1.append(word1.count(s1[i]))
            l2.append(word2.count(s2[i]))
        l1 = sorted(l1)
        l2 = sorted(l2)

        if l1!=l2:
            return False

        return True