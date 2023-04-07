class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        source = set()
        end = set()
        for s, e in edges:
            source.add(s)
            end.add(e)
        
        for i in end:
            if i in source:
                source.remove(i)

        return list(source)
            