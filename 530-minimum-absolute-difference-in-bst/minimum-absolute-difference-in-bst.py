# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root):
            if not root:
                return 0
            helper(root.left)
            res.append(root.val)
            helper(root.right)
            
        res = []
        helper(root)
        ans = float('inf')
        for i in range(0,len(res)-1):
            ans = min(ans,abs(res[i]-res[i+1]))
        return ans