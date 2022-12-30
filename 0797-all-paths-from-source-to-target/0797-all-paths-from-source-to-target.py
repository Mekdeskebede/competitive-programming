class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        stack = [(0, [0])]
        target = len(graph) - 1
        while stack:
            cur,route = stack.pop()
            if cur == target:
                result.append(route)
            else:
                for node in graph[cur]:
                    stack.append((node, route + [node]))
        return result