# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rows = defaultdict(list)
        
        def traverse(root,row,col):
            
            if root:
                traverse(root.left,row+1,col-1)
                rows[row].append(root.val)
                traverse(root.right,row+1,col+1)
        traverse(root,0,0)
        ans = []
        rows = OrderedDict(sorted(rows.items()))
        for key, val in rows.items():
            ans.append(val)
        return ans