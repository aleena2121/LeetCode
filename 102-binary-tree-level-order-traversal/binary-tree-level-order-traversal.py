# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(queue,value):
            if not queue:
                return None
            val = []
            level = []
            for i in queue:
                if i.left is not None:
                    level.append(i.left)
                    val.append(i.left.val)
                if i.right is not None:
                    level.append(i.right)
                    val.append(i.right.val)
            if len(val) != 0:
                value.append(val)
            queue = level
            return queue

        if root is None:
            return []

        queue = [root]
        value = [[root.val]]
        while queue:
            queue = bfs(queue,value)
        
        return value