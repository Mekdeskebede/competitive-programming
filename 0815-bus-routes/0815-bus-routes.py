class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj_list = defaultdict(set)
        for i, route in enumerate(routes):
            for r in route:
                adj_list[r].add(i)
                
        queue = deque([[source,0]])
        visited = set([source])
        seen_root = set()
        while queue:
            node, distance = queue.popleft()
            if node == target:
                return distance
            for root in adj_list[node]:
                if root not in seen_root:
                    for neighbor in routes[root]:
                        if neighbor not in visited:
                            queue.append([neighbor,distance+1])
                            visited.add(neighbor)
            seen_root.add(root)
        return -1