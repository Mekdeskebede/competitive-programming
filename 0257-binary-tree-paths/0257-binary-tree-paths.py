# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def traverse(root,temp):
            if root:
                temp.append(str(root.val))
                if not root.left and not root.right:
                    ans.append(temp[:])
                    temp.pop()
                traverse(root.left,temp[:])
                traverse(root.right,temp[:])
        
        traverse(root,[])  
        ans = ["->".join(i) for i in ans ]
    
        return ans