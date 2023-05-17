class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)
        incoming = [0] * n
        mht = []
        if not len(edges):
            return [0]
        
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
            incoming[start] += 1
            incoming[end] += 1
            
        queue = deque()
        for i in range(n):
            if incoming[i] == 1:
                queue.append(i)
                
        while queue:
            m = len(queue)
            mht = []
            for i in range(m):
                node = queue.popleft()
                mht.append(node)
                for neighbor in adj_list[node]:
                    incoming[neighbor] -= 1
                    if incoming[neighbor] == 1:
                        queue.append(neighbor)
                
        return mht
        