class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        
        additive = []
        def backtrack(idx):
            nonlocal n
            
            if idx >= n:
                return (len(additive) > 2) and (additive[-1] == additive[-2]+additive[-3])
            
            for i in range(idx,n):
                curr = int(num[idx:i+1])
                if len(additive) < 2 or curr == (additive[-1] + additive[-2]):
                    additive.append(curr)
                    if num[idx] == "0" and int(curr) > 0:
                        additive.pop()
                        continue
                    if backtrack(i + 1):
                        return True
                    additive.pop()
            return False
        
        return(backtrack(0)) 