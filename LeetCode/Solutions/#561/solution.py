class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        # Sort nums
        nums.sort()
        
        # Iterate over nums calculating sum of each pair
        totalSum = 0
        numsLen = len(nums)
        
        for i in range(0, numsLen - 1, 2):
            totalSum += nums[i]
        
        return totalSum
