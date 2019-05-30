# 7. Reverse Integer
## Problem
[Link](https://leetcode.com/problems/reverse-integer/)
## Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        # Convert to string
        xStr = str(x)
        
        # Reverse string then convert back to int
        # - is a special case that must be handled
        if "-" not in xStr:
            result = int(xStr[::-1])
        else:
            xStr = xStr[1::]
            result = int("-" + xStr[::-1])
            
        # Check for overflows
        if result > 2 ** 31 - 1:
            result = 0
        elif result < -2 ** 31:
            result = 0
        return result
```
