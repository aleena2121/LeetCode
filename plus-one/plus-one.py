class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        new_list = map(str, digits)
        string_value = ''.join(new_list)
        number = int(string_value)
        
        number = number + 1
        
        res = [int(x) for x in str(number)]
        
        return res