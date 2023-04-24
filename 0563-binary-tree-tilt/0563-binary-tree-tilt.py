# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.sum += abs(left - right)
            return left + right + root.val
        dfs(root)
        return self.sum