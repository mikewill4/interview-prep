# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Helper
    def hasPathSumHelper(self, root: TreeNode, sum: int, currSum: int) -> bool:
        if root is None:
            return False
        
        currSum += root.val
        
        left = right = False
        if root.left is None and root.right is None:
            return currSum == sum
        if root.right is not None:
            right = self.hasPathSumHelper(root.right, sum, currSum)
        if root.left is not None:
            left = self.hasPathSumHelper(root.left, sum, currSum)
        return left or right
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.hasPathSumHelper(root, sum, 0)
