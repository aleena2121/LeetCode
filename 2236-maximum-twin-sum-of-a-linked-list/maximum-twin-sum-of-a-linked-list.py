# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow
        prev = None
        curr = mid

        while mid:
            curr = mid
            mid = mid.next
            curr.next = prev
            prev = curr
        l1 = head
        l2 = prev
        max_sum = float("-inf")
        while l1 and l2:
            max_sum = max(max_sum,(l1.val + l2.val))
            l1 = l1.next
            l2 = l2.next
        
        return max_sum