# 107. Binary Tree Level Order Traversal II
## Problem
[Link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
## Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Utility function to get height of tree
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # Utility function to get the nodes of a single level
    def getLevelNodes(self, root: TreeNode, level: int, nodes: list) -> List[int]:
        if root is None:
            return
        elif level == 1:
            nodes.append(root.val)
        if level > 1:
            self.getLevelNodes(root.left, level - 1, nodes)
            self.getLevelNodes(root.right, level - 1, nodes)
        return nodes

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        height = self.height(root)
        traversal = []
        for level in range(height, 0, -1):
            traversal.append(self.getLevelNodes(root, level, []))
        return traversal
```
