# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        stack = []
        
        def dfs(root):
            if not root:
                return
            stack.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            if not root.left and not root.right:
                self.ans += int("".join(stack))
            stack.pop()
            
        dfs(root)
        return self.ans