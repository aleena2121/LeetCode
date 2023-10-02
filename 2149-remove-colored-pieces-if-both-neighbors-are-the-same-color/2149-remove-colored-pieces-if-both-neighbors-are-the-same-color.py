class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        c = list(colors)
        a = 0
        b = 0
        for i in range(1,len(c)-1):
            if c[i-1] == c[i] == c[i+1] == "A":
                a +=1
            if c[i-1] == c[i] ==  c[i+1] == "B":
                b +=1
        if a>b:
            return True
        else:
            return False