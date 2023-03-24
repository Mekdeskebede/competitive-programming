class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = set()
        
        for i in range(len(nums)):
    
            while (i + 1) != nums[i]:
                temp = nums[i]-1
                if nums[i] == nums[temp]:
                    ans.add(nums[i])
                    break
                nums[i], nums[temp] = nums[temp], nums[i]
                
        return list(ans)