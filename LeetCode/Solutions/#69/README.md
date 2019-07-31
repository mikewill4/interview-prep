# 69. Sqrt(x)
## Problem
[Link](https://leetcode.com/problems/sqrtx/)
## Solution
Here is my first submission, which works but is too slow to pass some of the
tests:
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        bigger = False
        curr_num = 0
        while not bigger:
            curr_square = curr_num ** 2
            if curr_square > x:
                bigger = True
            else:
                curr_num += 1
        return curr_num - 1
```
Here is my second submission, which is much faster and uses binary search:
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        min_val = 1
        max_val = x // 2
        result = 0
        while min_val <= max_val:
            mid = min_val + (max_val - min_val) // 2
            if mid <= x // mid:
                min_val = mid + 1
                result = mid
            else:
                max_val = mid - 1
        return result
```
