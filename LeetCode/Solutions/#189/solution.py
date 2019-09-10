class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        numsLen = len(nums)
        
        k %= numsLen
        
        start = numsLen - k
        otherNums = []
        count = 0
        for i in range(start, numsLen):
            otherNums.append(nums[count])
            nums[count] = nums[i]
            count += 1
        
        for i in range(numsLen - k):
            if k + i < start and nums[k + i] not in otherNums:
                otherNums.append(nums[k + i])
            nums[k + i] = otherNums[i]
