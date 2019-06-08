# 21. Merge Two Sorted Lists
## Problem
[Link](https://leetcode.com/problems/merge-two-sorted-lists/)
## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Special cases
        if l1 == None and l2 == None:
            return []
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        mergedHead = merged = None
        currL1 = l1
        currL2 = l2
        if currL1.val < currL2.val:
            mergedHead = merged = l1
            currL1 = currL1.next
        else:
            mergedHead = merged = l2
            currL2 = currL2.next
        while currL1 != None and currL2 != None:
            if currL1.val < currL2.val:
                merged.next = currL1
                currL1 = currL1.next
            else:
                merged.next = currL2
                currL2 = currL2.next
            merged = merged.next
        if currL1 != None:
            merged.next = currL1
        else:
            merged.next = currL2
        return mergedHead
```
