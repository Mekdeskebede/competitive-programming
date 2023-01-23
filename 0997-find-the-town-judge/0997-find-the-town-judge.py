class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusts = defaultdict(int)
        bieng_trusted = defaultdict(int)
        
        for a,b in trust:
            trusts[a] += 1 
            bieng_trusted[b] += 1
        
        for i in range(1,n+1):
            if trusts[i]==0 and bieng_trusted[i] == n-1:
                return i
        
        return -1
            
            
        
        