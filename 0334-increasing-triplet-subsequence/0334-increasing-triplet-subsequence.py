class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum = float("inf")
        second = float("inf")
        for num in nums:
            if num > second:
                return True
            if num <= minimum:
                minimum = num
            else:
                second = num
                
        return False