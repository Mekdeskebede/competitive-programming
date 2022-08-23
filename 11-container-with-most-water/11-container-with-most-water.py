class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        left_pointer = 0
        right_pointer = len(height) -1
        
        while left_pointer < right_pointer:
            
            
            
            if height[left_pointer] < height[right_pointer]:
                max_area = max(max_area, (right_pointer - left_pointer) * height[left_pointer])
                left_pointer += 1
            else:
                max_area = max(max_area, (right_pointer - left_pointer) * height[right_pointer])
                right_pointer -= 1
        return max_area
        