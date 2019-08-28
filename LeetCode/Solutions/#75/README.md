# 75. Sort Colors
## Problem
[Link](https://leetcode.com/problems/sort-colors/)
## Solution
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for value in nums:
            counts[value] += 1
                    
        numsLen = len(nums)
        for i in range(0,numsLen):
            if i < counts[0]:
                nums[i] = 0
            elif i < counts[0] + counts[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        
        return nums
```
