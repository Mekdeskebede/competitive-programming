# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def dfs(node,currSum):
            nonlocal ans
            if not node:
                return
            currSum += node.val
            
            if currSum == targetSum:
                ans += 1
            
            dfs(node.left,currSum)
            dfs(node.right,currSum)
            
        def helper(node):
            dfs(node,0)
            if node:
                helper(node.left)
                helper(node.right)
            
        helper(root)
        
        return ans