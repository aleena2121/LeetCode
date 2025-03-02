class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        res = []
        for i,j in nums1:
            if i not in hashmap:
                hashmap[i] = j
            else:
                hashmap[i] += j
        for i,j in nums2:
            if i not in hashmap:
                hashmap[i] = j
            else:
                hashmap[i] += j
        for i in hashmap:
            arr = [i,hashmap[i]]
            res.append(arr)
        return sorted(res)