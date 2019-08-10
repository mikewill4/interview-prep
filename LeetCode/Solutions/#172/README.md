# 172. Factorial Trailing Zeroes
## Problem
[Link](https://leetcode.com/problems/factorial-trailing-zeroes/)
## Solution
```python
class Solution:
	def trailingZeroes(self, int: n) -> int:
		numZeroes = count = 0
		while count <= n:
			if count % 5 == 0:
				numZeroes += 1
			if count % 25 == 0:
				numZeroes += 1
		return numZeroes
```
