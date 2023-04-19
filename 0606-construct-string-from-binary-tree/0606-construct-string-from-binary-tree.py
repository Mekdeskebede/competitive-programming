# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.curr = ""
        
        def dfs(root):
            if not root:
                return 
            self.curr += str(root.val)
            if not root.left and not root.right:
                return
            self.curr += "("
            dfs(root.left)
            self.curr += ")"
            if root.right:
                self.curr += "("
                dfs(root.right)
                self.curr += ")"
                
        dfs(root)
        return self.curr