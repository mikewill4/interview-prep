class Solution:
    
    def swap(self, start, end, s):
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        start += 1
        end -= 1
    
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        end = len(s) - 1
        start = 0
        vowels = "aeiouAEIOU"
        
        while start <= end:
            if s[start] in vowels:
                if s[end] in vowels:
                    self.swap(start, end, s)
                    start += 1
                    end -= 1
                else:
                    end -= 1
            elif s[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        
        return ''.join(s)
