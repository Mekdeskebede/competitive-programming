# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([[root,0]])
        max_ = 0
        while queue:
            
            left = 0
            right = 0
            level = len(queue)
            for i in range(len(queue)):
                node,idx = queue.popleft()
                if i == 0:
                    left = idx
                if i ==  level-1:
                    right = idx
                if node.left:
                    queue.append([node.left,idx*2])
                if node.right:
                    queue.append([node.right,idx*2+1])
            max_ = max(max_,right - left + 1)
            
        return max_
                    