# 28. Implement strStr()
## Problem
[Link](https://leetcode.com/problems/remove-element/)
## Solution
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
```
