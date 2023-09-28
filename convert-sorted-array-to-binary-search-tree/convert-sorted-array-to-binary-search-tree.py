# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build_bst(left, right):
            if left > right:
                return None
            
            mid = (left+right)//2
            root = self.TreeNode(nums[mid])
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            return root
        
        if not nums:
            return None
        
        return build_bst(0, len(nums) - 1)