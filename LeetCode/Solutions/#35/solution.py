class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            middle = left + ((right - left) // 2)
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return left
