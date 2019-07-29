# 38. Count and Say
## Problem
[Link](https://leetcode.com/problems/count-and-say/)
## Solution
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"
        for count in range(n - 1):
            curr_num = seq[0]
            next_num = 0
            new_seq = ""
            for index,ch in enumerate(seq):
                if ch == curr_num:
                    next_num += 1
                else:
                    new_seq += str(next_num)
                    new_seq += str(curr_num)
                    next_num = 1
                    curr_num = ch
            if next_num > 0:
                new_seq += str(next_num)
                new_seq += str(curr_num)
            seq = new_seq
        return seq
```
