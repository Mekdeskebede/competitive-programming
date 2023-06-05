# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def tree(root,val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = tree(root.left,val)
            else:
                root.right = tree(root.right,val)
            return root
        
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            tree(root,preorder[i])
            
        return root