# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, mini, maxi):
            maxi = max(maxi, node.val)
            mini = min(mini, node.val)
            self.ans = max( self.ans , abs( maxi - mini ) )
            if node.left:
                dfs(node.left, mini, maxi)
            if node.right:
                dfs(node.right, mini, maxi)
        
        dfs(root, root.val, root.val)

        return self.ans