# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def is_valid(node, left, right):
            if node is None:
                return True
            if not (left < node.val < right): 
                return False
            
            return is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right)
        
        return is_valid(root, float("-inf"), float("inf"))