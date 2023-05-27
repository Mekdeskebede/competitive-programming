class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum, middle = float('inf'), float('inf')
        for num in nums: 
            if num <= minimum: 
                minimum = num
            elif num <= middle:
                middle = num
            else:
                return True
        return False