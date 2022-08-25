class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = list(range(1,n+1))
        
        while len(queue) != 1 and queue:
            remove = k
            while remove > 0:
                temp = queue[0]
                queue.pop(0)
                queue.append(temp)
                

                remove -= 1
            queue.pop()
            
            
            
        return queue[0]
            