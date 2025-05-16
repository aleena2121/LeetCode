# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, traverse):
            if root is None:
                return
            inorder(root.left,traverse)
            traverse.append(root.val)
            inorder(root.right,traverse)
        
        traverse = []
        inorder(root,traverse)
        return traverse[k-1]
