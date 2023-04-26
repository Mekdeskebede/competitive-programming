"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.post = []
        def postOrder(node):
            if node:
                for child in node.children:
                    postOrder(child)
                self.post.append(node.val)
        postOrder(root)
        return self.post