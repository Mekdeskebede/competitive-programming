# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        root1 = root.left
        root2 = root.right
        def symmetric(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            left1 = symmetric(root1.left,root2.right)
            right2 = symmetric(root2.left,root1.right)
            
            return left1 and right2
        
        return symmetric(root1,root2)
            