class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v,w))
        distances = [float("inf")] * n
        distances[k-1] = 0
        visited = [False]*n
        heap = [[0,k]]
        
        while heap:
            weight, node = heapq.heappop(heap)
            if visited[node-1]:
                continue
            visited[node-1] = True
            for child,w in adj_list[node]:
                distance = weight + w
                if distance < distances[child-1]:
                    distances[child-1] = distance
                    heapq.heappush(heap, (distance, child))
                      
        return max(distances) if max(distances) != float("inf") else -1
                    
            
        