# 9. Palindrome Number
## Problem
[Link](https://leetcode.com/problems/palindrome-number/)
## Solution
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        if "-" in xStr:
            return False
        startIndex = 0
        endIndex = len(xStr) - 1
        while startIndex < endIndex:
            if xStr[startIndex] != xStr[endIndex]:
                return False
            startIndex += 1
            endIndex -= 1
        return True
```
