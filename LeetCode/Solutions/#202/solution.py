class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = []
        
        while True:
            
            # Compute sum of square of digits
            curr_sum = 0
            for digit in str(n):
                curr_sum += (int(digit) ** 2)
            n = curr_sum
            
            # Check if 1
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.append(n)
