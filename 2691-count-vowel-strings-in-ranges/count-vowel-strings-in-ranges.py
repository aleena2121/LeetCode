class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        n = len(words)
        
        val = [0] * n
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                val[i] = 1
        
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + val[i - 1]
        
        ans = [0] * len(queries)
        for i, (a, b) in enumerate(queries):
            ans[i] = prefix_sum[b + 1] - prefix_sum[a]
        
        return ans