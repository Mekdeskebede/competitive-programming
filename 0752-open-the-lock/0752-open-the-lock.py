class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        directions = [[1,0,0,0],[-1,0,0,0],[0,1,0,0],[0,-1,0,0],[0,0,1,0],[0,0,-1,0],[0,0,0,1],[0,0,0,-1]]
        visited = set()
        target = [int(i) for i in target]
        for slot in deadends:
            slot = [int(i) for i in slot]
            visited.add(tuple(slot))
        if (0,0,0,0) in visited:
            return -1
        queue = deque([[[0,0,0,0],0]])
        visited.add((0,0,0,0))
        while queue:
            node, distance = queue.popleft()
            if node == target:
                return distance
            for d in directions:
                temp = []
                for i in range(4):
                    temp.append((node[i]+d[i])%10)
                
                if tuple(temp) not in visited:
                    queue.append([temp,distance+1])
                    visited.add((tuple(temp)))
        return -1