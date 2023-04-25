# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_order = defaultdict(list)
        
        def dfs(node,row):
            if not node:
                return 
            level_order[row].append(node.val)
            dfs(node.left,row+1)
            dfs(node.right, row+1)
            
        dfs(root,0)
        ans = []
        for key,val in level_order.items():
            ans.append(sum(val)/len(val))
            
        return ans