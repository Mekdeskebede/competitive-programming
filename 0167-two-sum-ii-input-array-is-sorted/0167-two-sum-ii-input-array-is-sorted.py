class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        left = 0
        right = n - 1
        
        while left < right:
            
            add = numbers[left] + numbers[right]
            
            if  add == target:
                return [left+1, right+1]
            
            elif add < target:
                left += 1
                
            else: 
                right -= 1