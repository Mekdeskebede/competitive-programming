# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def traverse(node):
            if not node:
                return
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            traverse(node.left)
            traverse(node.right)
            
        traverse(root)
        queue = deque([[target.val,1]])
        visited = set()
        visited.add(target.val)
        res = []
        
        if k == 0:
            return [target.val]
        
        while queue:
            node,distance = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if distance == k:
                        res.append(neighbor)
                    queue.append([neighbor, distance+1])
                    visited.add(neighbor)
        return res
