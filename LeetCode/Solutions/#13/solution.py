class Solution:
    def romanToInt(self, s: str) -> int:
        strLen = len(s)
        result = 0
        for counter, value in enumerate(s):
            if value == "I":
                # Value of 1
                result += 1
            elif value == "V":
                # Check if I before it
                if counter - 1 >= 0 and s[counter - 1] == "I":
                    result += 3
                else:
                    # Value of 5
                    result += 5
            elif value == "X":
                # Check if I before it
                if counter - 1 >= 0 and s[counter - 1] == "I":
                    result += 8
                else:
                    # Value of 5
                    result += 10
            elif value == "L":
                # Check if X before it
                if counter - 1 >= 0 and s[counter - 1] == "X":
                    result += 30
                else:
                    # Value of 5
                    result += 50
            elif value == "C":
                # Check if X before it
                if counter - 1 >= 0 and s[counter - 1] == "X":
                    result += 80
                else:
                    # Value of 5
                    result += 100
            elif value == "D":
                # Check if C before it
                if counter - 1 >= 0 and s[counter - 1] == "C":
                    result += 300
                else:
                    # Value of 5
                    result += 500
            else:
                # Check if C before it
                if counter - 1 >= 0 and s[counter - 1] == "C":
                    result += 800
                else:
                    # Value of 5
                    result += 1000
        return result
