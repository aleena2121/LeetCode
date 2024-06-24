# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
       
        if not root:
            return []

        self.ans = []
        
        def bfs(root):
            queue = deque([root])
            while queue:
                level = []
                level_length = len(queue)
                for _ in range(level_length):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                self.ans.append(level)
        bfs(root)
        res = []
        for i in self.ans:
            res.append(float(float(sum(i))/len(i)))
        
        return res