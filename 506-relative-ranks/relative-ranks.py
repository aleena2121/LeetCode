class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = score[:]
        sorted_score = sorted(score, reverse = True)
        pos = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(sorted_score)):
            index = score.index(sorted_score[i])
            if i<3:
                res[index] = pos[i]
            else:
                res[index] = str(i+1)
            score[index] = None
        return res