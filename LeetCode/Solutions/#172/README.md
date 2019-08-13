# 172. Factorial Trailing Zeroes
## Problem
[Link](https://leetcode.com/problems/factorial-trailing-zeroes/)
## Solution
```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        numZeroes = 0
        if n < 5:
            return 0
        while n > 0:
            numZeroes += n // 5
            n //= 5
        return numZeroes
```
