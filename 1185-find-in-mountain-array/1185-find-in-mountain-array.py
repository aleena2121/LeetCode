# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:


class Solution:
    def findInMountainArray(self, target, mountainArr):
        n = mountainArr.length()
        maxPosition = -1
        left = 1
        right = n - 2
        while left < right:
            mid = left + (right - left) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        maxPosition = left
        left = 0
        right = maxPosition
        while left <= right:
            mid = left + (right - left) // 2
            me = mountainArr.get(mid)
            if me == target:
                return mid
            if me > target:
                right = mid - 1
            else:
                left = mid + 1
        left = maxPosition
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            me = mountainArr.get(mid)
            if me == target:
                return mid
            if me < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1