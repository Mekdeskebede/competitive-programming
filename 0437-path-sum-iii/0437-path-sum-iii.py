# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def helper(node, target):
            if not node:
                return 
            elif node.val==target:
                self.res+=1
            helper(node.left, target-node.val)
            helper(node.right, target-node.val)
            
        def dfs(root, target):
            if not root:
                return 
            helper(root, target)
            dfs(root.left, target)
            dfs(root.right,target)
            
        dfs(root, targetSum)
        return self.res