class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        incoming = []
        n = len(graph)
        ans = []
        queue = deque()
        
        for i in range(n):
            incoming.append(len(graph[i]))
            if incoming[i] == 0:
                queue.append(i)
                ans.append(i)
            for outgoing in graph[i]:
                adj_list[outgoing].append(i)
                
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                    ans.append(neighbor)
                    
        ans.sort()
        return ans
                    
                    
                    
            
        