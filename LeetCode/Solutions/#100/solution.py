# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None or p.val != q.val:
            return False
        left_value = self.isSameTree(p.left, q.left)
        right_value = self.isSameTree(p.right, q.right)
        return right_value and left_value
