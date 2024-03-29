# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = tmp = None
        curr = head
        
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
