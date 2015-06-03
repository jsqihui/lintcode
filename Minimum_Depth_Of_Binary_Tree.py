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
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        _, minDepth = self.helper(root)
        return minDepth
    
    def helper(self, root):
        if not root:
            return None, 0
        
        left, minLeft = self.helper(root.left)
        right, minRight = self.helper(root.right)
        
        if left and right:
            return root, min(minLeft, minRight) + 1
        elif left:
            return root, minRight + 1
        elif right:
            return root, minLeft + 1
        else:
            return root, 1

