class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = math.inf
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                add = nums[i]+nums[l]+nums[r]
                
                if abs(target-add)<abs(target-res) :
                    res = add
                
                if add<target :
                    l+=1
                elif target<add :
                    r-=1
                else :
                    return add
                    
        return res