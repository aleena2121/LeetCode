# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        new_node = TreeNode(root.val)
        new_node.right = self.invertTree(root.left)
        new_node.left = self.invertTree(root.right)
        return new_node