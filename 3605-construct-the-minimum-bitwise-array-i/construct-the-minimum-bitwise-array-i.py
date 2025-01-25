class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            j = 0
            satisfied = 0
            while j != i:
                if j | (j+1) == i:
                    ans.append(j)
                    satisfied = 1
                    break
                j+=1
            if satisfied == 0:
                ans.append(-1)

        return ans
                