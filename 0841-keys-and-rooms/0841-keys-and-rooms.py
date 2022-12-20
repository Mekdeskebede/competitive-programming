class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()

        def dfs(node):
        
            if node in seen:
                return
            
            seen.add(node)
            
            for i in rooms[node]:
                dfs(i)
        
        dfs(0)

        return len(seen) == len(rooms)