class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1)<len(nums2):
            k=nums1
            l=nums2
        else:
            k=nums2
            l=nums1
        for i in range (0,len(k)):
            if k[i] in l:
                res.append(k[i])
                l.remove(k[i])
                
        return res
                