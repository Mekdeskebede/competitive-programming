class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        cities = set()
        for path in paths:
            cities.add(path[0])
            
        for city in paths:
            if city[1] not in cities:
                return city[1]