class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Using Kadane's algorithm
        length = len(nums)
        for i in range(1, length):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
