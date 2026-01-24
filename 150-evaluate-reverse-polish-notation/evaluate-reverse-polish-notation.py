class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for tok in tokens:
            if tok not in "+-*/":
                nums.append(int(tok))
            else:                    
                num1 = nums.pop()    
                num2 = nums.pop()
                if tok == "+":
                    nums.append(num1 + num2)
                if tok == "-":
                    nums.append(num2 - num1)
                if tok == "*":
                    nums.append(num1 * num2)
                if tok == "/":
                    nums.append(int(num2 / num1))
        return nums[-1]