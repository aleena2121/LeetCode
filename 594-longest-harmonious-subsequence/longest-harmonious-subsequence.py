class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        max_cnts = 0
        for num, cnt in cnts.items():
            if num - 1 in cnts:
                max_cnts = max(max_cnts, cnt + cnts[num-1])
        return max_cnts
        