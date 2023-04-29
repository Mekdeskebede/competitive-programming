# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.diff = list()
    def inorderTraversal(self,root):
        if root:
            self.inorderTraversal(root.left)
            self.diff.append(root.val)
            self.inorderTraversal(root.right)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if (root == None):
            return False
        self.inorderTraversal(root)
        n = len(self.diff)
        for i in range(n):
            for j in range(i+1,n):
                if(self.diff[i]+self.diff[j]==k):
                    return True
        