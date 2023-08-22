from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        incoming = defaultdict(int)
        outgoing = defaultdict(list)
        for u,v in edges:
            incoming[v] += 1
            outgoing[u].append(v)
        ans = [1] * n
        q = deque()
        for i in range(1,n+1):
            if i not in incoming:
                q.append(i)
        
        time = 1
        while q:
            level = len(q)
            for _ in range(level):
                node = q.popleft()
                ans[node-1] = time
                for child in outgoing[node]:
                    incoming[child] -= 1
                    if incoming[child] == 0:
                        q.append(child)
            time += 1
        return ans
            
            
        
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends