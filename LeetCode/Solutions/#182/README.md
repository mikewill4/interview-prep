# 182. Duplicate Emails
## Problem
[Link](https://leetcode.com/problems/duplicate-emails/)
## Solution
```sql
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1;
```
