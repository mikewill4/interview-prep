class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for index, value in enumerate(nums):
            if index != 0 and value == nums[index - 1]:
                return True
        
        return False
