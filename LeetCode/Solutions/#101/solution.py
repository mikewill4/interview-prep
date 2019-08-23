# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Utility method for computing height of tree
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
    # Utility function for getting a particular level of nodes
    def getLevelNodes(self, root: TreeNode, level: int, nodes: list) -> list:
        if root is None:
            nodes.append(None)
        elif level == 1:
            nodes.append(root.val)
        elif level > 1:
            self.getLevelNodes(root.left, level - 1, nodes)
            self.getLevelNodes(root.right, level - 1, nodes)
        return nodes
    
    def isSymmetric(self, root: TreeNode) -> bool:
        height = self.height(root)
        for level in range(1, height + 1):
            # Get the nodes for the current level
            currLevelNodes = self.getLevelNodes(root, level, [])
            # Check that current level of nodes is a "palindrome"
            start = 0
            end = len(currLevelNodes) - 1
            while start <= end:
                if currLevelNodes[start] != currLevelNodes[end]:
                    return False
                start += 1
                end -= 1
        return True
