# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root1,root2):
            
            if not root1 and not root2:
                return True
            if not root1:
                return False
            if not root2:
                return False
        
            if root1.val != root2.val:
                return False
            if (dfs(root1.right,root2.left) and dfs(root1.left,root2.right)) or dfs(root1.right,root2.right) and dfs(root1.left,root2.left):
                return True
        
        return dfs(root1,root2)
                