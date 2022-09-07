class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        right = 0
        count = 1
        max_pick = 1
        
        while count < len(fruits):
            if (left == right) and (fruits[count] != fruits[left]):
                right = count
                
            elif (fruits[count] != fruits[left]) and (fruits[count] != fruits[right]):
                max_pick = max(max_pick, count - left)
                left = right 
                count = right
            count += 1
            
        final = max(max_pick, count - left)
        return final