# 26. Remove Duplicates from Sorted Array
## Problem
[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
## Solution
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length > 1:
            ptrOne = 0
            ptrTwo = 1
            while ptrTwo < length:
                while ptrTwo < length and nums[ptrOne] == nums[ptrTwo]:
                    ptrTwo += 1
                if ptrTwo < length:
                    nums[ptrOne + 1] = nums[ptrTwo]
                    ptrOne += 1
            return ptrOne + 1     
        else:
            return length
```
