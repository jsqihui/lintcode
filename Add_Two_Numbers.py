# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        
        if not l1:
            return l2
        if not l2:
            return l1

        carrier = 0
        ret = ListNode(0)
        dummy = ret
        while l1 and l2:
            sum_value = l1.val + l2.val + carrier
            ret.next = ListNode(sum_value % 10)
            carrier = sum_value / 10
            ret = ret.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_value = l1.val + carrier
            ret.next = ListNode(sum_value % 10)
            carrier = sum_value / 10
            ret = ret.next
            l1 = l1.next
        
        while l2:
            sum_value = l2.val + carrier
            ret.next = ListNode(sum_value % 10)
            carrier = sum_value / 10
            ret = ret.next
            l2 = l2.next
        
        if carrier != 0:
            ret.next = ListNode(carrier)
        
        return dummy.next

