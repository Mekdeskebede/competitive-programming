# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = []
        if n % 2 == 0:
            return []
        if n == 1:
            node = TreeNode(0)
            return [node]
        ans = []
        for i in range(1,n):
            if i % 2 == 0:
                continue
            left_tree = self.allPossibleFBT(i)
            right_tree = self.allPossibleFBT(n-i-1)

            for l in left_tree:
                for r in right_tree:
                    ans.append(TreeNode(0, l, r))
                    
        return ans