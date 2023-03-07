# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val,None)
        def insert(root):
            if root and not root.right and root.val < val:
                root.right = TreeNode(val,None)

            if root and not root.left and root.val > val:
                root.left = TreeNode(val,None) 
                
            if not root:
                return 
            
            if root.val < val:
                insert(root.right)
            else:
                insert(root.left)
        insert(root)
        return root