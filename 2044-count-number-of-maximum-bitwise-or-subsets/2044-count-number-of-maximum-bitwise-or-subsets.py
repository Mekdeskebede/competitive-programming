class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        self.subsets = defaultdict(int)
        
        def bitwiseOr(arr):
            bit = arr[0]
            for i in range(1,len(arr)):
                bit |= arr[i]
            return bit
        
        def backTrack(pointer,arr):
            if arr:
                self.subsets[bitwiseOr(arr[:])] += 1

            for num in nums[pointer:]:
                arr.append(num)
                backTrack(pointer+1,arr)
                arr.pop()
                pointer += 1
               
        backTrack(0,[])
                       
        return max(self.subsets.values())
                
            