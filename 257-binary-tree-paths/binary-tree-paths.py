# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
         
        def helper(root,res,ans):
            if root:
                if len(res)==0:
                    res+=str(root.val)
                else:
                    res+="->"+str(root.val)
                if not root.left and not root.right:
                    ans.append(res)
                left = helper(root.left,res,ans)
                right = helper(root.right,res,ans)


        ans = []
        helper(root,"",ans)
        return ans