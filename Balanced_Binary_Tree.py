"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        return abs(left - right) <= 1 and self.isBalanced(root.left) \
            and self.isBalanced(root.right)
        
    def depth(self, root):
        if not root:
            return 0
        
        return max(self.depth(root.left), self.depth(root.right)) + 1
            
