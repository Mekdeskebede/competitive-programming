class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for f, t , w in flights:
            adj_list[f].append((t,w))
            
        distances = [float("inf")] * n
        distances[src] = 0
        heap = [(0,0,src)]
        
        while heap:
            route, weight, node = heapq.heappop(heap)
            
            for child,w in adj_list[node]:
                distance = weight + w
                if distances[child] > distance and route <= k:
                    distances[child] = distance
                    heapq.heappush(heap,(route+1,distance,child))
        
        return distances[dst] if distances[dst] != float("inf") else -1
            
            
        