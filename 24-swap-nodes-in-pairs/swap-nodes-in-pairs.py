# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head2 = head.next
        curr = head
        prev = None
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            if prev:
                prev.next = temp
            prev = curr
            curr = curr.next
        return head2
