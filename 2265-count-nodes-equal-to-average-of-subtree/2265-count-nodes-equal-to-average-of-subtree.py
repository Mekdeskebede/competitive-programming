# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counts = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.counts = 0
        def traverse(root): 
            if not root:
                return (0,0)
            
            left,m_l = traverse(root.left)
            right,m_r = traverse(root.right)
            
            n = m_l + m_r + 1
            if (left + right + root.val)//n == root.val:
                self.counts += 1
            return (left + right + root.val,m_l + m_r + 1)
            
        traverse(root)
 
        return self.counts
                