# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        head1 = list1
        head2 = list2
        for i in range(a - 1):
            head1 = head1.next
        temp = head1
        for i in range(b - a + 1):
            temp = temp.next
        head1.next = list2
        while head2.next:
            head2 = head2.next
        head2.next = temp.next
        return list1