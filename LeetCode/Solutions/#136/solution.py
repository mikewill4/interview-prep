class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = []
        for i in nums:
            if i not in lookup:
                lookup.append(i)
            else:
                lookup.remove(i)
        return lookup[0]
