class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsets = []
    
        for start in range(len(nums)):  
            for end in range(start, len(nums)):  
                subsets.append(nums[start:end+1])
        cnt = 0
        for i in subsets:
            if len(i)==1:
                cnt = max(cnt,len(i))
            inc,dec = 0,0
            for j in range(0,len(i)-1):
                if i[j]<i[j+1]:
                    inc+=1
                elif i[j]>i[j+1]:
                    dec+=1
                if inc==len(i)-1 or dec==len(i)-1:
                    cnt = max(cnt, len(i))
        return cnt