class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def custom_sort_key(num):
            bit_count = bin(num).count('1')
            return (bit_count, num)

        arr.sort(key=custom_sort_key)

        return arr