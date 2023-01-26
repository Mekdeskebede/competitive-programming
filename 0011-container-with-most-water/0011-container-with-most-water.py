class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        left = 0
        right = n-1
        area = 0
        while left < right:
            
            area = max(area, (right-left) * min(height[left],height[right]))
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return area
            
            
        
        