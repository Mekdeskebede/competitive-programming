class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0, 10:0}
        for cost in bills:
            if cost == 5:
                changes[5] += 1
                continue
            if not changes[5]:
                return False
            if cost == 10:
                changes[5] -= 1
                changes[10] += 1
            else:
                if changes[10]:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True
                
                    
                    