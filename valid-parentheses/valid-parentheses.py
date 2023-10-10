class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in "([{": 
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    return False  
            elif i == "]":
                if not stack or stack.pop() != "[":
                    return False 
            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False  

        return not stack
