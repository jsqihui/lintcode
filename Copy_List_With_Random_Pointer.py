# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList_hqi(self, head):
        # write your code here
        # copy nodes first and use a hashmap
        # TLE
        node_map = {}
        dummy = head
        while head:
            new_head = RandomListNode(head.label)
            node_map[head] = new_head
            head = head.next
        
        head = dummy
        while head:
            if head.next:
                node_map[head].next = node_map[head.next]
            if head.random:
                node_map[head].random = node_map[head.random]
            
            head = head.next
        
        return node_map
    
    def copyRandomList(self, head):
        
        dummy = head
        while head:
            next = head.next
            new_head = RandomListNode(head.label)
            head.next = new_head
            new_head.next = next
            head = next
        
        head = dummy
        while head:
            next = head.next
            if head.random:
                next.random = head.random.next
            head = next.next
        
        new_head = dummy.next
        dummy = new_head
        while new_head and new_head.next:
            new_head.next = new_head.next.next
            new_head = new_head.next
        
        return dummy
