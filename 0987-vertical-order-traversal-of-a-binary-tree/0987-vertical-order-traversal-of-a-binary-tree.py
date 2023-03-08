# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(dict)
        
        def traverse(root,row,col):
            
            if root:
                traverse(root.left,row+1,col-1)
                if col in d and row in d[col]: 
                    d[col][row].append(root.val)
                else:
                    d[col][row] = [root.val]
                traverse(root.right,row+1,col+1)
                
        traverse(root,0,0)
        res = []
        d = OrderedDict(sorted(d.items()))
        for key, val in d.items():
            val = OrderedDict(sorted(val.items()))
            temp = []
            for k in val:
                temp += sorted(val[k])
            res.append(temp)

        return res
        
        