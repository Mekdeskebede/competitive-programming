# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        
        def dfs(node, left):
            
            if not node:
                return 
            if not node.left and not node.right and left:
                self.sum += node.val
                
            dfs(node.left, True)
            dfs(node.right, False)
            
            
        dfs(root, False)
        
        return self.sum
                