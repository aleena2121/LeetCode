# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        stack = []
        
        while temp:
            stack.append(temp.val)  
            temp = temp.next
        
        while head:
            if head.val != stack.pop(): 
                return False
            head = head.next
        
        return True
        
            
        
        