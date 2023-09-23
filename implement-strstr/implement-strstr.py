class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0  

        for j in range(len(haystack) - len(needle) + 1):
            if needle[0] == haystack[j]:
                found = True
                for i in range(1, len(needle)):
                    if needle[i] != haystack[j + i]:
                        found = False
                        break
                if found:
                    return j

        return -1