# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        curr = head.next
        prev = head
        
        while curr != None:
            if curr.val == prev.val:
                prev.next = curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
