class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        

     
        def greedy(i, j):
            
            if i==j: 
                return nums[i]
            
            player1 = nums[i]-greedy(i+1,j)
            player2 = nums[j]-greedy(i,j-1)
            
            return max(player1, player2)
        
        return True if greedy(0,len(nums)-1) >= 0 else False
    