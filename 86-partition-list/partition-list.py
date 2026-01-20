# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = ListNode()
        greater = ListNode()
        less = lesser
        great = greater

        curr = head
        while curr:
            next_node = curr.next      
            curr.next = None           

            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                great.next = curr
                great = great.next

            curr = next_node

        less.next = greater.next
        return lesser.next
