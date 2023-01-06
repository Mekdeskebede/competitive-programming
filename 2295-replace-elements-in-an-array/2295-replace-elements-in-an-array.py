class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        operation_map = {}
        for old, new in reversed(operations):
            operation_map[old] = operation_map.get(new,new)
        
        for idx,num in enumerate(nums):
            if num in operation_map:
                nums[idx] = operation_map[num]
                
        return nums