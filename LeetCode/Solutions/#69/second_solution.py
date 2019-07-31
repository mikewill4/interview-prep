class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        min_val = 1
        max_val = x // 2
        result = 0
        while min_val <= max_val:
            mid = min_val + (max_val - min_val) // 2
            if mid <= x // mid:
                min_val = mid + 1
                result = mid
            else:
                max_val = mid - 1
        return result
