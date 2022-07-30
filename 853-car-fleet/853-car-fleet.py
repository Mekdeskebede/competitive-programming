class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
   
        stack = []
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append([position[i],speed[i]])
        pos_speed.sort()
        for i in range(len(pos_speed)-1,-1,-1):
            stack.append((target-pos_speed[i][0])/pos_speed[i][1])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
                
        result = len(stack)
        return result 