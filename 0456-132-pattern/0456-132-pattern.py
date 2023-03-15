class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        mid_num = float("-inf")
        stack = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < mid_num:
                return True
            while stack and stack[-1] < nums[i]:
                mid_num = stack.pop()
            stack.append(nums[i])
        return False