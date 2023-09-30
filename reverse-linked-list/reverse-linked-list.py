# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if not stack:
            return None
        new_head = stack.pop()
        curr = new_head
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        
        curr.next = None
        
        return new_head
        