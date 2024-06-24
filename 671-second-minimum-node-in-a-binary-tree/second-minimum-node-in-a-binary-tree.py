# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            if root.val not in self.stack:
                self.stack.append(root.val)
            left = dfs(root.left)
            right = dfs(root.right)
        
        self.stack = []
        dfs(root)
        min_ = min(self.stack)
        self.stack.remove(min_)
        if len(self.stack)==0:
            return -1
        return (min(self.stack))