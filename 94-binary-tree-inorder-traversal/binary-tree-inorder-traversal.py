# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(self,root,s):
            if root.left!=None:
                inorder(self,root.left,s)
            s.append(root.val)
            if root.right!=None:
                inorder(self,root.right,s)
        s = []
        if root==None:
            return []
        inorder(self,root,s)
        return s