class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        res1 = []
        res2 = []
        for i in nums1:
            if i not in nums2:
                res1.append(i)
        for i in nums2:
            if i not in nums1:
                res2.append(i)
        
        return [res1,res2]