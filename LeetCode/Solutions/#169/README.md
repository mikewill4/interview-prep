# 169. Majority Element
## Problem
[Link](https://leetcode.com/problems/majority-element/)
## Solution
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
```
