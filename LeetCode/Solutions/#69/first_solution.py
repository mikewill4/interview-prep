class Solution:
    def mySqrt(self, x: int) -> int:
        bigger = False
        curr_num = 0
        while not bigger:
            curr_square = curr_num ** 2
            if curr_square > x:
                bigger = True
            else:
                curr_num += 1
        return curr_num - 1
