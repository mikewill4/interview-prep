# 258. Add Digits
## Problem
[Link](https://leetcode.com/problems/add-digits/)
# Solution
```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            new_num = 0
            curr_num = num
            while curr_num != 0:
                new_num += (curr_num % 10)
                curr_num //= 10
            return self.addDigits(new_num)
```
