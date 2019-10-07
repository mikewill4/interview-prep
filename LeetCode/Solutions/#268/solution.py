class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        found = [False] * (len(nums) + 1)
        
        for value in nums:
            found[value] = True
        
        missing_index = -1
        
        for index, val in enumerate(found):
            if not val:
                missing_index = index
                break
        
        return missing_index
