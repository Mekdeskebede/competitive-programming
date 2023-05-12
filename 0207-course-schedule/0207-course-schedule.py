class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        count = [0] * numCourses
        
        for start, end in prerequisites:
            adj_list[start].append(end)
            count[end] += 1
            
        queue = deque()
        for i in range(numCourses):
            if not count[i]:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                count[neighbor] -= 1
                if count[neighbor] == 0:
                    queue.append(neighbor)
                    
        for cnt in count:
            if cnt > 0:
                return False
        return True
            