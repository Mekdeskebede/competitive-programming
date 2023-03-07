# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSame(p,q):
            if not q and p or not p and q:
                return False
            
            if not q and not p:
                return True
            
            if q.val != p.val:
                return False
            
            return isSame(p.left,q.left) and isSame(p.right,q.right)
            
        return isSame(p,q)
     
        