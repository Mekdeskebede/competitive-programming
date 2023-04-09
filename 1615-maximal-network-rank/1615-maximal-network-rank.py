class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        
        for road in roads:
            adj_list[road[0]].append(road[1])
            adj_list[road[1]].append(road[0])
            
        max_rank = 0
        for city in adj_list:
            for pair_city in adj_list:
                if city == pair_city:
                    continue
                    
                connected = False
                for p in adj_list[city]:
                    if p == pair_city:
                        connected = True
                        break
                        
                if connected:
                    max_rank = max(max_rank,len(adj_list[city])+len(adj_list[pair_city])-1)
                else:
                    max_rank = max(max_rank,len(adj_list[city])+len(adj_list[pair_city]))
        
        return max_rank
                