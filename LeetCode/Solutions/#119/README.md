# 119. Pascal's Triangle II
## Problem
[Link](https://leetcode.com/problems/pascals-triangle-ii/)
## Solution
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currRow = []
        prevRow = []
        for row in range(1, 35):
            prevRow = currRow
            currRow = []
            if len(prevRow) < 2:
                for col in range(1, row + 1):
                    currRow.append(1)
            else:
                for col in range(1, row + 1):
                    if col == 1 or col == row:
                        currRow.append(1)
                    else:
                        currRow.append(prevRow[col - 2] + prevRow[col - 1])
            if row == rowIndex + 1:
                return currRow
        return []
```
