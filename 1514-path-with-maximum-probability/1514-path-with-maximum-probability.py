class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            adj_list[edges[i][0]].append((edges[i][1],succProb[i]))
            adj_list[edges[i][1]].append((edges[i][0],succProb[i]))
            
        distances = [0] * n
        distances[start_node] = 0
        visited = [False]*n
        heap = [[1,start_node]]
        
        while heap:
            weight, node = heapq.heappop(heap)
            if weight < 0:
                weight = -weight
            if visited[node]:
                continue
            visited[node] = True
            for child,w in adj_list[node]:
                
                distance = weight * w
                if distance > distances[child]:
                    distances[child] = distance
                    heapq.heappush(heap, (-distance, child))
                    
        return distances[end_node]