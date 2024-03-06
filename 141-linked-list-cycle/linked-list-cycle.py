# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        first = head
        second = head
        
        while first and first.next:
            first = first.next.next
            second = second.next
            
            if first == second:
                return True
        
        return False