class Solution:
    def __init__(self):
        self.res = []
    def getRow(self, rowIndex: int) -> List[int]: 
        def recur(n,path,rowIndex):
        
            if rowIndex == -1:
                self.res = path.copy()
                return 
            if not path:
                ans = [1]
            elif path == [1]:
                ans = [1,1]
            else:
                ans = [0] * (n+1)
                for i in range(n+1):
                    if i == 0 or i == n:
                        ans[i] = 1
                    else:
                        ans[i] = path[i-1] + path[i]
            recur(n + 1, ans,rowIndex - 1)
            
            
        recur(0,[],rowIndex)
        return self.res
        
        
        
        