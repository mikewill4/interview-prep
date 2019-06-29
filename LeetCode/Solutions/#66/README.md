## 66. Plus One
# Problem
[Link](https://leetcode.com/problems/plus-one/)
# Solution
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if digits[length - 1] == 9:
            curr = length - 1
            while digits[curr] == 9:
                digits[curr] = 0
                curr -= 1
            if curr < 0:
                new_digits = []
                new_digits.append(1)
                for i in range(0,length):
                    new_digits.append(0)
                return new_digits
            else:        
                digits[curr] += 1
        else:
            digits[length - 1] += 1
        return digits
```
