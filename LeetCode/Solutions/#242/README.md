# 242. Valid Anagram
## Problem
[Link](https://leetcode.com/problems/valid-anagram/)
## Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
