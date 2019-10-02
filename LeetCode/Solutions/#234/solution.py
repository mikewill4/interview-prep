# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        seen = []
        curr = head
        end = 0
        
        # Add elements to list
        while curr != None:
            seen.append(curr.val)
            curr = curr.next
            end += 1
        
        # Do normal palindrome algorithm
        start = 0
        end -= 1
        
        while start <= end:
            if seen[start] != seen[end]:
                return False
            start += 1
            end -= 1
            
        return True
