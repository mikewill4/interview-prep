# 155. Min Stack
## Problem
[Link](https://leetcode.com/problems/min-stack/)
## Solution
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sortedStack = []
        self.otherStack = []
        self.size = 0

    def push(self, x: int) -> None:
        curr = 0
        while curr < self.size and x < self.sortedStack[curr]:
            curr += 1
        self.sortedStack.insert(curr, x)
        self.otherStack.append(x)
        self.size += 1

    def pop(self) -> None:
        elem = self.otherStack.pop()
        self.sortedStack.remove(elem)
        self.size -= 1

    def top(self) -> int:
        return self.otherStack[self.size - 1]

    def getMin(self) -> int:
        return self.sortedStack[self.size - 1]
```
