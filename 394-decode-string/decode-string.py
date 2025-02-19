class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        temp = ""

        for i in s:
            if i.isdigit():
                num = (num*10) + int(i)

            elif i=='[':
                stack.append((temp,num))
                num = 0
                temp = ""

            elif i==']':
                string,nums = stack.pop()
                temp = string + (temp*nums)
        
            else:
                temp += i
        return temp