class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n=len(questions)
        
        profit = [0]* n
        
        maximum = [0] * n
        
        profit[-1] = questions[-1][0]
        maximum[-1] = profit[-1]
        
        for i in range(n-1,-1,-1):
            
            profit[i] = questions[i][0]
            nextindex = i + questions[i][1]+1
            if nextindex<n:
                profit[i] += maximum[nextindex]
            if i!=n-1:
                maximum[i] = max(maximum[i+1],profit[i])
        return maximum[0]