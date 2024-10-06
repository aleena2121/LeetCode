class Solution(object):
    def areSentencesSimilar(self, s1, s2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        sen1 = s1.split()
        sen2 = s2.split()

        n1 = len(sen1)
        n2 = len(sen2)

        if n1 > n2:
            sen1, sen2 = sen2, sen1
            n1, n2 = n2, n1
        
        start, end = 0, 0

        while start < n1 and sen1[start] == sen2[start]:
            start += 1

        while end < n1 and sen1[n1 - end - 1] == sen2[n2 - end - 1]:
            end += 1
            
        return start + end >= n1