# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode()
        y = dummy
        a = head.next
        val = 0
        while (a):
            if a.val!=0:
                val+=a.val
            else:
                y.next = ListNode(val)
                val = 0
                y = y.next
            a = a.next
        return dummy.next
