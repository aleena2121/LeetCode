# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
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
        for i in range(len(self.stack)-1):
            for j in range(i+1,len(self.stack)):
                if self.stack[i]+self.stack[j] == k:
                    return True
        
        return False