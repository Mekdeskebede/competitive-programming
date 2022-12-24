class Solution:
    def average(self, salary: List[int]) -> float:
        
        n = len(salary)
        mini = min(salary)
        maxi = max(salary)
        total = sum(salary) - mini - maxi
        ave = total/(n-2)
        
        return ave