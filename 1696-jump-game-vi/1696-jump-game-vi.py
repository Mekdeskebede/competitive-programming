class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        score_idx = defaultdict()
        res = nums[0]
        score_idx[nums[0]] = 0
        i = 0
        
        for idx, value in enumerate(nums):
            
            if i == 0:
                i += 1
                continue

            while score_idx and (score_idx[list(score_idx.keys())[0]] < idx-k):
                score_idx.pop(list(score_idx.keys())[0])
           
            res =  value + list(score_idx.keys())[0] 
            
            while score_idx and res >= list(score_idx.keys())[-1]:
                score_idx.pop(list(score_idx.keys())[-1])
                
            score_idx[res] = idx
            i +=1
  
        return res
                
           

                    

                        
                    
                
        
        
        