"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        return self.helper(A, 0, len(A) - 1)
    
    def helper(self, A, start, end):
        if start > end:
            return None
        
        mid = start + (end - start) / 2
        root = TreeNode(A[mid])
        
        root.left = self.helper(A, start, mid - 1)
        root.right = self.helper(A, mid + 1, end)
        
        return root
