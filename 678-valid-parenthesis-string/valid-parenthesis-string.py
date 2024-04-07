class Solution(object):
    def checkValidString(self, s):
        stack = []
        for i in s:
            if i == "(" or i == "*" :
                stack.append(i)
            elif i == ")":
                if stack and (stack[-1] == "(" or stack[-1] == "*"):
                    stack.pop()
                else:
                    return False
        stack = []
        for i in reversed(s):
            if i == ")" or i == "*":
                stack.append(i)
            elif i == "(":
                if stack and (stack[-1] == ")" or stack[-1] == "*"):
                    stack.pop()
                else:
                    return False
        return True