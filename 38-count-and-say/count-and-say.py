class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s):
            arr = []
            for i in s:
                if len(arr) > 0 and arr[-1][1] == i:
                    arr[-1][0] += 1
                else:
                    arr.append([1,i])
            return arr
        
        def make_string(arr):
            res = ""
            for i in arr:
                res += str(i[0]) + str(i[1])
            return res
        
        res = "1"
        for i in range(n-1):
            arr = count(res)
            res = make_string(arr)
        
        return res