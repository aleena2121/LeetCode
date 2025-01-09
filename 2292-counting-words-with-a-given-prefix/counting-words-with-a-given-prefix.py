class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            if pref in words[i]:
                word = words[i]
                if pref == word[:len(pref)]:
                    res+=1
        return res