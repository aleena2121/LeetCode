class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def backtrack(i,j,k):
            if (i,j) in memo:
                return memo[(i,j)]
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and s1[i]==s3[k]:
                if (backtrack(i+1,j,k+1)):
                    memo[(i,j)] = True
                    return True

            if j < len(s2) and s2[j]==s3[k]:
                if (backtrack(i,j+1,k+1)):
                    memo[(i,j)] = True
                    return True
            memo[(i,j)] = False
            return False
        memo = {}
        if len(s1)+len(s2) != len(s3):
            return False
        return backtrack(0,0,0)