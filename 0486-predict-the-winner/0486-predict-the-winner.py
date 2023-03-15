class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def winner(nums,left,right):
            if left >right:
                return 0
            
            start = nums[left] + min(winner(nums,left+2,right), winner(nums,left+1,right-1))
            end = nums[right] + min(winner(nums,left+1,right-1), winner(nums,left,right-2))
    
            return max(start,end)
        
        player1 = winner(nums,0,n-1)
        total = sum(nums)
        return player1 >= total - player1