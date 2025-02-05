class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        ind = []
        cnt = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                cnt+=1
                ind.append(i)
        if cnt>2:
            return False
        else:
            if len(ind)==1:
                return False
            if s1[ind[0]] == s2[ind[1]] and s2[ind[0]] == s1[ind[1]]:
                return True
        return False