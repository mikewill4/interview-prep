# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Height utility function
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
