class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowel = []
        s_list = list(s)
        for i in s_list:
            if i in vowels:
                vowel.append(i)
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowel[-1]
                vowel.pop()

        s = "".join(s_list) 
        return s
            
