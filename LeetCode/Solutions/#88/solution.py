class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr_one = ptr_two = 0
        if n != 0:
            while ptr_one < m + n:
                curr1 = nums1[ptr_one]
                curr2 = nums2[ptr_two]
                if ptr_one >= m:
                    nums1[ptr_one] = curr2
                    ptr_one += 1
                    ptr_two += 1
                elif curr2 >= curr1:
                    ptr_one += 1
                else:
                    if curr1 > nums2[-1]:
                        nums2.append(curr1)
                    else:
                        for i in range(ptr_two, len(nums2)):
                            if nums2[i] >= curr1:
                                nums2.insert(i, curr1)
                                break
                    nums1[ptr_one] = curr2
                    ptr_two += 1
