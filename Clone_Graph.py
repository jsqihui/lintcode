# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None

        queue = [node]
        nodeMap = {node:UndirectedGraphNode(node.label)}
        start = 0
        # clone node
        while start < len(queue):
            s = queue[start]
            start += 1
            for n in s.neighbors:
                if n not in nodeMap:
                    nodeMap[n] = UndirectedGraphNode(n.label)
                    queue.append(n)

        # clone edge
        for n in queue:
            for nb in n.neighbors:
                nodeMap[n].neighbors.append(nodeMap[nb])
        
        return nodeMap[node]
        
