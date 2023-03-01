class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        max_window = 0
        unique = defaultdict(int)
        left = 0
        
        for right in range(n):
            unique[fruits[right]] += 1
            
            while len(unique) > 2:
                unique[fruits[left]] -= 1
                if unique[fruits[left]] <= 0:
                    del unique[fruits[left]]
                left += 1
            
            max_window = max(max_window, right-left+1)
        
        return max_window
        
        