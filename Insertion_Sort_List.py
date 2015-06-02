""" TLE, it works with java version but TLE with python ""
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
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        
        dummy = ListNode(0)
        
        while head:
            node = dummy
            while node.next and node.next.val < head.val:
                node = node.next
            
            temp = head.next
            head.next = node.next
            node.next = head
            head = temp
        
        return dummy.next
                
        
        

