class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        tasks = Counter(tasks)
        
        ans =  0
        for key, val in tasks.items():
            
            if val < 2:
                return -1
            else:
                ans += val//3 
                if val%3 != 0:
                    ans += 1
        
        return ans