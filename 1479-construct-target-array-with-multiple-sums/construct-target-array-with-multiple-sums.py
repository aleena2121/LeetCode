import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-x for x in target]
        heapq.heapify(heap)

        total = sum(target)

        while True:
            max_val = -heapq.heappop(heap)
            rest_sum = total - max_val

            if max_val == 1 or rest_sum == 1:
                return True
            if rest_sum == 0 or max_val <= rest_sum:
                return False

            prev = max_val % rest_sum
            if prev == 0:
                return False

            heapq.heappush(heap, -prev)
            total = rest_sum + prev