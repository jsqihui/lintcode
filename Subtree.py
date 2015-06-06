"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if not T1 and not T2:
            return True
        
        if not T1:
            return False

        if self.isIdentical(T1, T2):
            return True
        
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def isIdentical(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
