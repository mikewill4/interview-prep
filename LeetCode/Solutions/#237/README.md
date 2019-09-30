# 237. Delete Node in a Linked List
## Problem
[Link](https://leetcode.com/problems/delete-node-in-a-linked-list/)
## Solution
```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
