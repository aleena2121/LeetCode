from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = defaultdict(list)
    
        for i in nums:
            num = i
            sum = 0
            while i>0:
                sum += int(i%10)
                i//=10
            if sum not in digit_sum:
                digit_sum[sum] = [num]
            else:
                digit_sum[sum].append(num)
        max_sum = -1
        for i,j in digit_sum.items():
            if len(j)>=2:
                j.sort(reverse=True)
                max_sum = max(max_sum,j[0]+j[1])
        return max_sum