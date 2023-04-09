"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adj_list = defaultdict(list)
        self.importance = 0
        
        for employee in employees:
            adj_list[employee.id] = [employee.importance] + employee.subordinates
        
        def dfs(id):
            self.importance += adj_list[id][0]   
            
            for i in range(1,len(adj_list[id])):
                dfs(adj_list[id][i])
        
        dfs(id)
        
        return self.importance
            
            
            