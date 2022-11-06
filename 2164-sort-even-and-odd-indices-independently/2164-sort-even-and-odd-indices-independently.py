class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = [nums[i] for i in range(len(nums)) if i%2 != 0]
        even = [nums[i] for i in range(len(nums)) if i%2 == 0]
        odd.sort(reverse = True)
        even.sort()
        length = max(len(odd), len(even))
        res = []
        for i in range(length):
            if i < len(even):
                res.append(even[i])
            if i < len(odd):
                res.append(odd[i])
        return res