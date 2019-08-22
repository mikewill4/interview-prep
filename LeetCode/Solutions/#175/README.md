# 175. Combine Two Tables
## Problem
[Link](https://leetcode.com/problems/combine-two-tables/)
## Solution
```sql
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address ON Address.PersonId = Person.PersonId;
```
