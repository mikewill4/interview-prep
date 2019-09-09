# 176. Second Highest Salary
## Problem
[Link](https://leetcode.com/problems/second-highest-salary/)
## Solution
```sql
SELECT MAX(Salary) SecondHighestSalary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee)
```
