class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        running_sum = 0
        
        remainder_index = {0 : -1}

        for i in range(len(nums)):
            running_sum += nums[i]
            r = running_sum % k
            if r in remainder_index:
                if i - remainder_index[r] >= 2:
                    return True
            else:
                remainder_index[r] = i
        
        return False
