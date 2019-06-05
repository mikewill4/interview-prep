class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        openParen = ["(", "{", "["]
        closeParen = [")", "}", "]"]
        for value in s:
            paren.append(value)
            if value in closeParen:
                currValue = paren.pop()
                if len(paren) > 0:
                    prevValue = paren.pop()
                    if currValue == ")" and prevValue != "(":
                        return False
                    elif currValue == "}" and prevValue != "{":
                        return False
                    elif currValue == "]" and prevValue != "[":
                        return False
                else:
                    return False
        return len(paren) == 0
