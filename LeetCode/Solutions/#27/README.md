# 27. Remove Element
## Problem
[Link](https://leetcode.com/problems/remove-element/)
## Solution
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        ptrOne = ptrTwo = 0
        while ptrTwo < length:
            if nums[ptrTwo] != val:
                nums[ptrOne] = nums[ptrTwo]
                ptrOne += 1
            ptrTwo += 1
        return ptrOne
```
