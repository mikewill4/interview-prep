class Solution:
    def titleToNumber(self, s: str) -> int:
        s_len = len(s)
        curr = col_num = 0
        while curr < s_len - 1:
            col_num += ((ord(s[curr]) - 64) * 26 ** (s_len - curr - 1))
            curr += 1
        return col_num + (ord(s[curr]) - 64)
