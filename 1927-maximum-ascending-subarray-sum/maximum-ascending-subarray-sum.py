class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
        max_sum = float('-inf')
        sum_i = 0
        for start in range(len(nums)):
            for end in range(start,len(nums)):
                sub.append(nums[start:end+1])
        for i in sub:
            if len(i)==1:
                sum_i=sum(i)
            else:
                for j in range(len(i)-1):
                    if i[j]>=i[j+1]:
                        sum_i = float('-inf')
                        break
                    else:
                        sum_i=sum(i)
            max_sum = max(max_sum,sum_i)

        return max_sum