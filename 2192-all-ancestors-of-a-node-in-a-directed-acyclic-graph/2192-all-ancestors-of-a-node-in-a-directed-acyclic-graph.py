class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adj_list = defaultdict(list)
        outgoing = defaultdict(int)
        ans = [set() for i in range(n)]
        
        for start, end in edges:
            adj_list[start].append(end)
            outgoing[end] += 1
            
        queue = deque()
        for i in range(n):
            if not outgoing[i]:
                queue.append(i)
    
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                ans[neighbor].update(ans[node])
                ans[neighbor].add(node)
                outgoing[neighbor] -= 1
                if outgoing[neighbor] == 0:
                    queue.append(neighbor)

        for i in range(n):
            ans[i] = list(ans[i])
            ans[i].sort()
        
        return ans