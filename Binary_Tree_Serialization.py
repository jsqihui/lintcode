""" level order traversal, failed with last test
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        result = ""
        if not root:
            return result
        queue = [root]
        nodeLeft = True
        while queue and nodeLeft:
            size = len(queue)
            nodeLeft = False
            for i in range(size):
                node = queue.pop(0)
                result += str(node.val)
                if node.left:
                    nodeLeft = True
                    queue.append(node.left)
                else:
                    queue.append(TreeNode("#"))
                if node.right:
                    nodeLeft = True
                    queue.append(node.right)
                else:
                    queue.append(TreeNode("#"))

        return result
        

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        i = 0
        root = TreeNode(data[i])
        current_queue = [root]
        while current_queue:
            size = len(current_queue)
            if i >= len(data) - 1:
                break
            for j in range(size):
                node = current_queue.pop(0)
                if node is None:
                    i += 2
                    left = None
                    right = None
                else:
                    i += 1
                    if data[i] == "#":
                        left = None
                    else:
                        left = TreeNode(data[i])

                    i += 1
                    if data[i] == "#":
                        right = None
                    else:
                        right = TreeNode(data[i])

                    node.left = left
                    node.right = right
                current_queue.append(left)
                current_queue.append(right)

        return root
            
            
            

