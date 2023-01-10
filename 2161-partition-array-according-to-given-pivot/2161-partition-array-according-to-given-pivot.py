class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        equals = []
        smaller = []
        greater = []
        
        for num in nums:
            if num == pivot:
                equals.append(num)
            elif num < pivot:
                smaller.append(num)
            else:
                greater.append(num)
                
        res = smaller + equals + greater
        return res