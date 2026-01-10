from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) < len(nums2):
            first, second = nums1, nums2
        else:
            first, second = nums2, nums1

        count = defaultdict(int)
        for i in first:
            count[i] += 1
        
        for i in second:
            if count[i] > 0:
                res.append(i)
                count[i] -= 1
        
        return res
    