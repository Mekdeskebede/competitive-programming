class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj_list = defaultdict()
        cities = set()
        for path in paths:
            adj_list[path[0]] = path[1]
            cities.add(path[0])
            cities.add(path[1])
            
        for city in cities:
            if city not in adj_list:
                return city