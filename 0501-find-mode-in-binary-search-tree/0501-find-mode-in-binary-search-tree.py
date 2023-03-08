# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = defaultdict(int)
        
        def inorderTraverse(root):
            
            if root:
                inorderTraverse(root.left)
                count[root.val] += 1
                inorderTraverse(root.right)
                
        inorderTraverse(root)        
        ans = []
        max_val = max(count.values())
        
        for key in count:
            if count[key] == max_val:
                ans.append(key)
                
        return ans
                