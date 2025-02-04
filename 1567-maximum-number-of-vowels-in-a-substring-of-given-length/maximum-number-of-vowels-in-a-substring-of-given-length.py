class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        max_cnt = 0

        for i in range(k):
            if s[i] in vowels:
                cnt+=1

        max_cnt = cnt

        for i in range(k,len(s)):
            if s[i] in vowels:
                cnt+=1
            if s[i-k] in vowels:
                cnt-=1
            max_cnt = max(max_cnt,cnt)

        return max_cnt