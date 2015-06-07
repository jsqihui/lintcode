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
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        level = 0
        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.pop(0)
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = level + 1
            if level % 2:
                result.append(row)
            else:
                result.append([e for e in reversed(row)])
        return result
                

