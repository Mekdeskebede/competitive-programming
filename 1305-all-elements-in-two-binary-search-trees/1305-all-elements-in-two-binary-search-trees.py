# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        list1 = []
        list2 = []
        
        def traverse1(node):
            if node:
                traverse1(node.left)
                list1.append(node.val)
                traverse1(node.right)
        
        def traverse2(node):
            if node:
                traverse2(node.left)
                list2.append(node.val)
                traverse2(node.right)
                
        traverse1(root1)
        traverse2(root2)
        ans = []
        p1 = 0
        p2 = 0
        
        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] < list2[p2]:
                ans.append(list1[p1])
                p1 += 1
            else:
                ans.append(list2[p2])
                p2 += 1
        ans.extend(list1[p1:])
        ans.extend(list2[p2:])
        
        return ans

            
        