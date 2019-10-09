class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = []
        
        for num in nums1:
            try:
                num_index = nums2.index(num)
                intersection.append(num)
                nums2[num_index] = -1
            except:
                # Catch exception and move on
                num_index = -1
        
        return intersection
