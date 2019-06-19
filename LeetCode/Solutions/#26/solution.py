class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length > 1:
            ptrOne = 0
            ptrTwo = 1
            while ptrTwo < length:
                while ptrTwo < length and nums[ptrOne] == nums[ptrTwo]:
                    ptrTwo += 1
                if ptrTwo < length:
                    nums[ptrOne + 1] = nums[ptrTwo]
                    ptrOne += 1
            return ptrOne + 1     
        else:
            return length
