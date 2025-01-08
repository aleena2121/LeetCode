class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        n = len(words)
        for i in range(n):
            w1 = words[i]
            for j in range(i+1,n):
                w2 = words[j]
                if len(w2)<len(w1):
                   continue 
                prefix = w2[:len(w1)]
                suffix = w2[-len(w1):]
                if prefix == w1 and suffix == w1:
                    ans+=1
        return ans