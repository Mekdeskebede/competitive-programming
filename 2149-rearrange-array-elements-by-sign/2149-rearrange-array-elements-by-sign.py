class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)//2
        positives = []
        negatives = []
        
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
                
        ans = []
        for idx in range(n):
            ans.append(positives[idx])
            ans.append(negatives[idx])
            
        return ans