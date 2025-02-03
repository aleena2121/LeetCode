class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_map = {}
        cnt = 0

        for i in nums:
            complement = k - i

            if complement in count_map and count_map[complement]>0:
                cnt+=1
                count_map[complement] -=1
            else:
                if i in count_map:
                    count_map[i] += 1
                else:
                    count_map[i] = 1
        return cnt