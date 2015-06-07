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
    def maxPathSum(self, root):
        # write your code here
        maxPath, _ = self.helper(root)
        return maxPath
        
    def helper(self, root):
        if not root:
            return -sys.maxint, 0
        
        # divide
        leftMax, leftSingle = self.helper(root.left)
        rightMax, rightSingle = self.helper(root.right)
        
        # conqure
        # get a single max path from leaf to root
        rootSingle = max(leftSingle, rightSingle) + root.val
        rootSingle = max(rootSingle, 0)
        rootMax = max(leftSingle + rightSingle + root.val, leftMax, rightMax)
        
        return rootMax, rootSingle
        

