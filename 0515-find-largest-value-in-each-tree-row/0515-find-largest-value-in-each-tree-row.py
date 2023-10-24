# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        r = []
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

        for i in res:
            r.append(max(i))

        return r    