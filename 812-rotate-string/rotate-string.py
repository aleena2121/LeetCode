class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)
        for _ in range(n):
            if s == goal:
                return True
            s = s[1:] + s[0]

        return False