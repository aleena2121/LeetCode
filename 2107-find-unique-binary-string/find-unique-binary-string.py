class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        for i in range(n):
            digit = nums[i][i]
            if digit == "1":
                ans.append("0")
            else:
                ans.append("1")
        return "".join(ans)