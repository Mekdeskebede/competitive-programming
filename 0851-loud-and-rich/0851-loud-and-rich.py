class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj_list = defaultdict(list)
        incoming = defaultdict(int)
        n = len(quiet)
        queue = deque()
        ans = [i for i in range(n)]
        
        for rich, poor in richer:
            adj_list[rich].append(poor)
            incoming[poor] += 1
        
        for i in range(n):
            if not incoming[i]:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                incoming[neighbor] -= 1
                if quiet[ans[neighbor]] >= quiet[ans[node]]:
                    ans[neighbor] = ans[node]
                if not incoming[neighbor]:
                    queue.append(neighbor)
                    
        return ans
                    
                    
            