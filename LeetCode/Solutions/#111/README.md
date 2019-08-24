# 111. Minimum Depth of Binary Tree
## Problem
[Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
## Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)
        
        if leftHeight == 0:
            return rightHeight + 1
        elif rightHeight == 0:
            return leftHeight + 1
        else:
            return min(leftHeight, rightHeight) + 1
```
