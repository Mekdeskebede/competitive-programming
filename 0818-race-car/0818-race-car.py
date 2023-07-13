class Solution:
    def racecar(self, target: int) -> int:
        def accelerate(pos,speed):
            return (pos+speed, speed*2)
        def reverse(speed):
            return -1 if speed > 0 else 1
        
        queue = deque([[[0,1],0]])
        while queue:
            node, step = queue.popleft()
            if node[0] == target:
                return step
            pos1, speed1 = accelerate(node[0], node[1])
            speed2 = reverse(node[1])
            queue.append([[pos1,speed1],step+1])
                
            if (pos1) < target and node[1] < 0 or (pos1) > target and node[1] > 0:
                    queue.append([[node[0],speed2],step+1])