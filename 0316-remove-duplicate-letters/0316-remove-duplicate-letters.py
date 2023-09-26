class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        char_count = {}
        included = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        result = []
        for char in s:
            char_count[char] -= 1
            if included.get(char, False):
                continue
            while result and char < result[-1] and char_count[result[-1]] > 0:
                included[result.pop()] = False
            result.append(char)
            included[char] = True
        return ''.join(result)
