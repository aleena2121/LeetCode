class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        map = {0:1}

        for i in nums:
            running_sum += i

            if running_sum - k in map:
                count += map[running_sum - k]
            
            if running_sum not in map:
                map[running_sum] = 1
            else:
                map[running_sum] += 1
        return count