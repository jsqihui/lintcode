"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(inorder) != len(preorder):
            return None
        length = len(inorder)
        return self.helper(inorder, 0, length - 1, preorder, 0, length - 1)


    def helper(self, inorder, istart, iend, preorder, pstart, pend):
        if istart > iend:
            return None
        
        root = TreeNode(preorder[pstart])
        imid = self.findRootIndex(inorder, istart, iend, preorder[pstart])
        
        root.left = self.helper(inorder, istart, imid - 1, 
                                preorder, pstart + 1, pstart + imid - istart)
        root.right = self.helper(inorder, imid + 1, iend,
                                 preorder, pstart + imid - istart + 1, pend)
        return root


    def findRootIndex(self, inorder, istart, iend, key):
        for i in range(istart, iend+1):
            if inorder[i] == key:
                return i
        

