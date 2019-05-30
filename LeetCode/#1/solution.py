class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for counter, value in enumerate(nums):
            if target - nums[counter] not in lookup:
                lookup[value] = counter
            else:
                return [lookup[target - nums[counter]], counter]
