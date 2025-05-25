# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 1
        curr = head
        while curr.next is not None:
            curr = curr.next
            length += 1
        k = k % length

        while k > 0:
            curr = head
            while curr.next and curr.next.next is not None:
                curr = curr.next
            last = curr
            last = curr.next
            curr.next = None
            last.next = head
            head = last
            k -= 1
        return head
            
