class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backTrack(pointer,arr):
            ans.append(arr[:])

            for num in nums[pointer:]:
                arr.append(num)
                backTrack(pointer+1,arr)
                arr.pop()
                pointer += 1
               
        backTrack(0,[])
        return ans