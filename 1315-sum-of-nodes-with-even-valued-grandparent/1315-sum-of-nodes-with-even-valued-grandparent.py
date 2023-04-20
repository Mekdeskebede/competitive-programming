# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(grandParent,parent,node):
            if not node:
                return
            if grandParent and grandParent % 2 == 0:
                self.ans += node.val
            dfs(parent,node.val,node.left)
            dfs(parent,node.val,node.right)
        
        dfs(None,None,root)
        return self.ans