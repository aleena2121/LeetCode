import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minheap = []
        cnt = 0
        for i in nums:
            heapq.heappush(minheap,i)

        while minheap:
            min1 = heapq.heappop(minheap)
            if min1>=k:
                break
            min2 = heapq.heappop(minheap)
            heapq.heappush(minheap,min(min1,min2)*2+max(min1,min2))
            cnt+=1
        return cnt