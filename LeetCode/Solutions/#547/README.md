# 547. Friend Circles
## Problem
[Link](https://leetcode.com/problems/friend-circles/)
## Solution
```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = []
        circles = 0
        for person,friends in enumerate(M):
            if person not in seen:
                circles += 1
                seen.append(person)
                
                # Queue
                friendsQueue = []
                friendsQueue.append(friends)
                
                while len(friendsQueue) != 0:
                    for index,friend in enumerate(friendsQueue.pop(0)):
                        if friend == 1 and index not in seen:
                            seen.append(index)
                            friendsQueue.append(M[index])
        return circles
```
