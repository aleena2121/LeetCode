# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        current = [root]

        while current:
            next_level = []
            values = []
            for node in current:
                values.append(node.val)
                if (node.left):
                    next_level.append(node.left)
                if (node.right):
                    next_level.append(node.right)
                
            res.append(values)
            current = next_level
            
        return res