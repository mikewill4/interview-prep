# 14. Longest Common Prefix
## Problem
[Link](https://leetcode.com/problems/longest-common-prefix/)
## Solution
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Special cases
        strListLen = len(strs)
        if strListLen == 0:
            return ""
        elif strListLen == 1:
            return strs[0]
        
        firstStr = strs[0]
        secondStr = strs[1]
        secondStrLen = len(secondStr)
        
        end = -1
        count = -1
        
        for counter,value in enumerate(firstStr):
            if counter >= secondStrLen or value != secondStr[counter]:
                end = counter
                break
            count = counter
        if count != -1:
            if end == -1:
                end = secondStrLen - 1
            for i in range(0,end+1):
                for s in range(0,strListLen-1):
                    if i >= len(strs[s]) or i >= len(strs[s + 1]) or strs[s][i] != strs[s + 1][i]:
                        return secondStr[:i]
            return firstStr
        else:
            return ""
```
