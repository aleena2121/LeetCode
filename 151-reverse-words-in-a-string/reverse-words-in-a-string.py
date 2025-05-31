class Solution:
    def reverseWords(self, s: str) -> str:
        s_ = s.split(" ")
        s_ = [i.strip() for i in s_ if i != '']
        return " ".join(reversed(s_))