"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
    
        return dummy

