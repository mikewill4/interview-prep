class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        new_arr = []
        for num2 in arr2:
            for num1 in arr1:
                if num1 == num2:
                    new_arr.append(num1)
                    
        
        # Add leftovers
        leftovers = []
        for num1 in arr1:
            if num1 not in new_arr:
                leftovers.append(num1)
        
        leftovers.sort()
        
        new_arr.extend(leftovers)
        
        return new_arr
