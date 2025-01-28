class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        maxlen = 0

        for i in s:
            if i == "(":
                left += 1
            else:
                right +=1
            if (left == right):
                maxlen = max(maxlen,left*2)
            elif (right>left):
                right,left = 0,0

        s = s[::-1]
        left = 0
        right = 0

        for i in s:
            if i == "(":
                left += 1
            else:
                right +=1
            if (left == right):
                maxlen = max(maxlen,left*2)
            elif (right<left):
                right,left = 0,0
        return maxlen