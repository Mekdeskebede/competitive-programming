class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        self.visited = set()
        adj_list = defaultdict(list)
        n = len(isConnected)
        group = 0
        
        for row in range(n):
            for col in range(n):
                if row == col:
                    continue
                if isConnected[row][col] == 1:
                    adj_list[row+1].append(col+1)
        
        def dfs(city):
            self.visited.add(city)
            for neighbor in adj_list[city]:
                if neighbor not in self.visited:
                    dfs(neighbor)
         
        for c in range(1,n+1):
            if c not in adj_list:
                group += 1
            elif c not in self.visited:
                group += 1 
                dfs(c)
                
        return group