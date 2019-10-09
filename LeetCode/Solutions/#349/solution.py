class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = []
        
        for num in nums1:
            if num not in intersection and num in nums2:
                intersection.append(num)
        
        return intersection
