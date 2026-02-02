class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        inc = False
        dec = False
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
            inc = True
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
            dec = True
        if inc and dec and i == len(arr) - 1:
            return True
        else:
            return False