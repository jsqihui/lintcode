"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        # find prev N node
        
        dummy = ListNode(0)
        dummy.next = head
        while n > 0:
            head = head.next
            n = n - 1
        
        prev = dummy
        while head:
            head = head.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next

