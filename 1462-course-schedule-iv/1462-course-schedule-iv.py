class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        
        for s,e in prerequisites:
            graph[s].append(e)
            incoming[e] += 1
        
        queue = deque()
        if prerequisites:
            for course in range(numCourses):
                if incoming[course] == 0:
                    queue.append(course)

        prereq = defaultdict(set)
        while queue:
            node = queue.popleft()
            for course in graph[node]:
                incoming[course] -= 1
                prereq[course].add(node)
                prereq[course].update(prereq[node])
                if incoming[course] == 0:
                    queue.append(course)
        ans = []
        for p,c in queries:
            ans.append(p in prereq[c])
        
        return ans
        
                
            