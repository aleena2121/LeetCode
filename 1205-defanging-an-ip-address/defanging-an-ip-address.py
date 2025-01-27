class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ""
        for i in address:
            if i.isnumeric():
                res += i
            else:
                res += "[.]"
        
        return res