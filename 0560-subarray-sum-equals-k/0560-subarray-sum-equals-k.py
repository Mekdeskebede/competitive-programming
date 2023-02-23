class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        diff = {0:1}
        
        prefix = []
        pre_sum = 0
        
        for num in nums:
            pre_sum += num
            
            prefix.append(pre_sum)
        
        subarrays = 0

        for pre in prefix:
            
            
            if pre - k in diff:
                # print(dict[pre - k])
                subarrays += diff[pre - k]
                
            diff[pre] = diff.get(pre,0) + 1
        
        return subarrays
                 
                

            

            
            
        