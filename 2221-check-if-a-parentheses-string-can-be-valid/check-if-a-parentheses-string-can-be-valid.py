class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        openbrackets = []
        unlocked = []
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                openbrackets.append(i)
            elif s[i] == ")":
                if openbrackets:
                    openbrackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while openbrackets and unlocked and openbrackets[-1] < unlocked[-1]:
            openbrackets.pop()
            unlocked.pop()

        if openbrackets:
            return False

        return True