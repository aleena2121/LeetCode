class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        res = 0
        end = float(-inf)
        for i in intervals:
            if i[0]<end:
                res+=1
            else:
                end = i[1]
        return res