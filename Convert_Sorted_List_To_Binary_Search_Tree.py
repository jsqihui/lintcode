"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        # the idea is to use inorder traversal, find the left most position
        # and start with the head node
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        size = 0
        runner = head
        while runner:
            size += 1
            runner = runner.next
        
        self.node = head
        return self.inorderHelper(0, size - 1)
    
    def inorderHelper(self, start, end):
        if start > end:
            return None
        
        mid = start + (end - start)/2
        left = self.inorderHelper(start, mid - 1)
        
        treeNode = TreeNode(self.node.val)
        treeNode.left = left
        self.node = self.node.next
        
        right = self.inorderHelper(mid + 1, end)
        treeNode.right = right
        return treeNode
        
