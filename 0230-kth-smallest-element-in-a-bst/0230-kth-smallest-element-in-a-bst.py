# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans  = 0
    k = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def traverse(root,k):
            if root:
                traverse(root.left,self.k)
                self.k -= 1
                if self.k == 0:
                    self.ans = root.val
                    return
                traverse(root.right,self.k)
                
        traverse(root,self.k)  
        return self.ans
 