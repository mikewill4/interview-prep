# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        visited = []
        
        while curr != None:
            if curr in visited:
                return True
            else:
                visited.append(curr)
                curr = curr.next
        return False
