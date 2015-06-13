"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        # assign right subtree to left and assign left subtree to right
        # don't assign directly because the root.left need to be used latter
        self.helper(root)
        
    
    def helper(self, root):
        if not root:
            return None
        
        left = self.helper(root.right)
        right = self.helper(root.left)

        root.left = left
        root.right = right
        return root

