class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        ALen = len(A)
        
        if ALen == 0 and len(B) == 0:
            return True
        
        for shift in range(1,ALen):
            A = A[:0] + A[1:ALen] + A[:1]
            if A == B:
                return True
        return False
