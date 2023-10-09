# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node,arr,currSum):
            if not node:
                return
            currSum += node.val
            arr.append(node.val)
            
            if not node.left and not node.right and currSum == targetSum:
                ans.append(arr[:])
            
            dfs(node.left,arr,currSum)
            dfs(node.right,arr,currSum)
            arr.pop()
            
        dfs(root,[],0)
        return ans
            
            
            
            
                
            