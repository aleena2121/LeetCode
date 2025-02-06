# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        res = int("".join(map(str,stack)),2)
        return res