class Solution:
    def isPalindrome(self, s: str) -> bool:
        isPal = True
        endIndex = len(s) - 1
        dontInc = False
        startIndex = 0
        while startIndex < endIndex:
            if s[startIndex] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                startIndex += 1
                continue
            if s[endIndex] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                endIndex -= 1
                continue
            if s[startIndex].lower() != s[endIndex].lower():
                isPal = False
                break
            endIndex -= 1
            startIndex += 1
        return isPal
