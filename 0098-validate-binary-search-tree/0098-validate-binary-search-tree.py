# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        minimum = -float(inf)
        maximum = float(inf)
        
        def valid(root,minimum,maximum):
            if not root:
                return True
            if minimum >= root.val or  root.val >= maximum:
                return False
            
            return valid(root.left,minimum,root.val) and valid(root.right,root.val,maximum)
            
        return valid(root,minimum,maximum)

