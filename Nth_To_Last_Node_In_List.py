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
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        dummy = head

        while n > 0:
            head = head.next
            n -= 1
        
        while head:
            dummy = dummy.next
            head = head.next
        
        return dummy

