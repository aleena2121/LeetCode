from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        length = 0
        center_used = False

        for word in list(freq.keys()):
            rev = word[::-1]
            if word != rev:
                pair_count = min(freq[word], freq[rev])
                length += pair_count * 4
                freq[word] -= pair_count
                freq[rev] -= pair_count
            
            else:
                pair_count = freq[word] // 2
                length += pair_count * 4
                freq[word] -= pair_count * 2
                if not center_used and freq[word] > 0:
                    length += 2
                    center_used = True 

        return length