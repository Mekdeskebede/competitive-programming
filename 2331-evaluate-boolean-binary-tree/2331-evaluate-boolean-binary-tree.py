# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val
        
        left = self.evaluateTree(root.left)
        right= self.evaluateTree(root.right)
        
        if root.val == 2:
            return left or right
        return left and right