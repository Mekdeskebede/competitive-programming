class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n not in visited:
            visited.append(n)
            temp = 0
            num = str(n)
            for i in range(len(num)):
                temp += int(num[i]) * int(num[i])
            if temp == 1:
                return True
            n = temp
            
            num = str(temp)