class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()
        n = len(nums)
        permutations = []
        
        def permutation(arr):
            
            if len(arr) == n:
                permutations.append(arr[:])
                
            for num in nums:
                if num not in seen:
                    arr.append(num)
                    seen.add(num)
                    permutation(arr)
                    seen.remove(arr.pop())
                    
        permutation([])
        return permutations
                
          