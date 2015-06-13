"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    # pay attention to the different index range
    def buildTree(self, inorder, postorder):
        # write your code here
        if len(inorder) != len(postorder):
            return None
        length = len(inorder)
        return self.helper(inorder, 0, length - 1, postorder, 0, length - 1)


    def helper(self, inorder, istart, iend, postorder, pstart, pend):
        if istart > iend:
            return None
        
        root = TreeNode(postorder[pend])
        imid = self.findRootIndex(inorder, istart, iend, postorder[pend])
        
        root.left = self.helper(inorder, istart, imid - 1, 
                                postorder, pstart, pstart + imid - istart -1)
        root.right = self.helper(inorder, imid + 1, iend,
                                 postorder, pstart + imid - istart, pend -1)
        return root


    def findRootIndex(self, inorder, istart, iend, key):
        for i in range(istart, iend+1):
            if inorder[i] == key:
                return i
        

