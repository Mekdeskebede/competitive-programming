class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i in range(len(bombs)):
            x1, y1, r1= bombs[i]
            for j in range(len(bombs)):
                x2, y2, r2= bombs[j]
                distance= sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                if i != j and distance <= r1:
                    adj_list[i].append(j)
        
        def dfs(node):
            nonlocal count
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    count += 1
                    dfs(neighbor)
        res= 0
        for i in range(len(bombs)):
            visited = set([i])
            count = 1
            dfs(i)
            res = max(res,count)
        return res
                    
        