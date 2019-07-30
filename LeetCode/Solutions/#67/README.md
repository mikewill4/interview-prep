# 67. Add Binary
## Problem
[Link](https://leetcode.com/problems/add-binary/)
## Solution
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length_a = len(a)
        length_b = len(b)
        if length_a < length_b:
            a = ((length_b - length_a) * "0") + a
            length_a = length_b
        else:
            b = ((length_a - length_b) * "0") + b
            length_b = length_a
        carry = 0
        final_sum = ""
        for i in range(length_a - 1, -1, -1):
            curr_sum = int(a[i]) + int(b[i]) + carry
            if curr_sum == 0:
                carry = 0
                final_sum = "0" + final_sum
            elif curr_sum == 1:
                carry = 0
                final_sum = "1" + final_sum
            elif curr_sum == 2:
                carry = 1
                final_sum = "0" + final_sum
            else:
                carry = 1
                final_sum = "1" + final_sum
        if carry != 0:
            final_sum = "1" + final_sum
        return final_sum
```
