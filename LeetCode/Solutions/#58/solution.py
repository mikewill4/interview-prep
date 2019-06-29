class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if words == None or len(words) == 0:
            return 0
        else:
            return len(words[len(words) - 1])
