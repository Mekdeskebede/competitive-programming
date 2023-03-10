# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = defaultdict(list)
        def traverse(root,row,col):
            if root:
                traverse(root.left,row+1,col-1)
                level[row].append(root.val) 
                traverse(root.right,row+1,col+1)
        
        traverse(root,0,0)
        level = OrderedDict(sorted(level.items()))
        ans = []
        for key, val in level.items():
            ans.append(val[-1])
            
        return ans
        
        