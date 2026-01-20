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

        while head != None:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            elif head.val >= x:
                great.next = ListNode(head.val)
                great = great.next
            head = head.next
        
        less.next = greater.next
        return lesser.next

