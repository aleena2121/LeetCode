class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        cnt = 0
        max_len = 0
        ind_zero = -1
        while j < len(nums):
            if nums[j] == 1:
                j+=1
            elif nums[j] == 0 and cnt < k:
                cnt += 1
                ind_zero = j
                j += 1
            else:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            max_len = max(max_len,j-i)
            
        return max_len
            