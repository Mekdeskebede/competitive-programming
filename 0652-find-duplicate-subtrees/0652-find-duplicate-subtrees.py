# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_map = defaultdict(list)
        ans = []
        
        def dfs(node):
            if not node:
                return "n"
            hashh = str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
            if len((hash_map[hashh])) == 1:
                ans.append(node)
            hash_map[hashh].append(node)
            return hashh
        
        dfs(root)
        
        return ans