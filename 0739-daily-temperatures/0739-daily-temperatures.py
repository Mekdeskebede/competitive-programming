class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_idx = [[n,i] for i, n in enumerate(temperatures) ]
        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            crr = temperatures[i]
            while stack and crr > stack[-1][0]:
                
                greater, greater_idx= stack.pop()
                # greater_idx =  temperatures.index(greater)
                result[greater_idx] = i-greater_idx
            stack.append([crr,i])
        return result