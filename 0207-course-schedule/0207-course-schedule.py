class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        outgoing = defaultdict(list)
        incoming = defaultdict(int)
        for a, b in prerequisites:
            adj_list[a].append(b)
            outgoing[b].append(a)
            incoming[a] += 1
        courses = set(i for i in range((numCourses)))
        queue = deque()
        for i in range(numCourses):
            if i not in adj_list:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            courses.remove(node)
            for child in outgoing[node]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
        if len(courses) == 0:
            return True
        return False
            
            