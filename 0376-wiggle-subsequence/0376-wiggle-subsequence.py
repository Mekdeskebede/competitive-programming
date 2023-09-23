class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        inc = [1]
        dec = [1]
        
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                inc.append(dec[i-1]+1) 
                dec.append(dec[i-1])
            elif nums[i] < nums[i-1]:
                dec.append(inc[i-1]+1) 
                inc.append(inc[i-1])
            else:
                inc.append(inc[i-1]) 
                dec.append(dec[i-1])
                
        return max(inc[-1], dec[-1])