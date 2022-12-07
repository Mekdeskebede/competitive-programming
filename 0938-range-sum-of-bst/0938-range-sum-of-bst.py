# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        n = [root]
        while n:
            curr = n.pop()
            if curr:
                if low <= curr.val <= high:
                    ans += curr.val
                if curr.val > low:
                    n.append(curr.left)
                if curr.val < high:
                    n.append(curr.right)
        return ans