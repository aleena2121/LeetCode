class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            for i in nums2:
                nums1.append(i)
            nums = sorted(nums1)
        else:
            for i in nums1:
                nums2.append(i)
            nums = sorted(nums2)
        
        if len(nums)%2!=0:
            return nums[(len(nums)//2)]
        else:
            return (nums[len(nums)//2]+nums[len(nums)//2-1])/2