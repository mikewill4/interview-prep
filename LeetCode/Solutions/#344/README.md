# 344. Reverse String
## Problem
[Link](https://leetcode.com/problems/reverse-string/)
## Solution
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end_index = len(s) - 1
        for start_index, value in enumerate(s):
            
            if start_index >= end_index:
                break
            
            tmp = value
            s[start_index] = s[end_index]
            s[end_index] = tmp
            
            end_index -= 1
```
