class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        """
        g=[]
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                g += ["FizzBuzz"]
            elif(i%3==0 and i%5!=0):
                g += ["Fizz"]
            elif(i%3!=0 and i%5==0):
                g += ["Buzz"]
            else:
                g.append(str(i))
        return g