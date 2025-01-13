class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        
        for char in freq:
            if freq[char] > 2:
                if freq[char]%2 == 0:
                    freq[char] = 2
                else:
                    freq[char] = 1
        
        return sum(freq.values())
