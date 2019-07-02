# 121. Best Time to Buy and Sell Stock
## Problem
[Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
## Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        minVal = maxVal = prices[0]
        maxProfit = 0
        for i in range(length):
            if prices[i] < minVal and i != length - 1:
                minVal = prices[i]
                maxVal = minVal
            if prices[i] > maxVal:
                maxVal = prices[i]
            if maxVal - minVal > maxProfit:
                maxProfit = maxVal - minVal
        return maxProfit
```
