# 283. Move Zeroes
## Problem
[Link](https://leetcode.com/problems/move-zeroes/)
## Solution
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        to_move = []
        
        for index, val in enumerate(nums):
            if val != 0:
                to_move.append(val)
                nums[index] = 0
        
        to_move_len = len(to_move)
        for i in range(to_move_len):
            nums[i] = to_move[i]
```
