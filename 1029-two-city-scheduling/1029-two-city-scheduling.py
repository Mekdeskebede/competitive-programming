class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i,(a,b) in enumerate(costs):
            diff.append([b-a,i])
            
        diff.sort()
        total_cost = 0
        
        for i in range(len(diff)//2):
            total_cost += costs[diff[i][1]][1]
            
        for j in range(len(diff)//2,len(diff)):
            total_cost += costs[diff[j][1]][0]
        
        return total_cost