class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        pos_speed = []
        
        for i in range(n):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort()
        
        stack = []
        for i in range(n-1,-1,-1):
            stack.append((target-pos_speed[i][0])/pos_speed[i][1])
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
                
            
            
                                                    