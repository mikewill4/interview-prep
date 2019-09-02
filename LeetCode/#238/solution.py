class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # With division
        product = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCount += 1
                
        output = []
        
        if zeroCount == 1:
            for num in nums:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            return output
        elif zeroCount > 1:
            return [0] * len(nums)
        
        for num in nums:
            output.append(product // num)
        
        return output
