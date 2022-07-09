class Solution(object):
    
#     def sorting(self,a):
#     # to sort an array
#         for i in range(len(a)):
#             for j in range(len(a)-1):
#                 if a[j+1] < a[j]:
#                     a[j+1],a[j] = a[j],a[j+1]

#                 else:
#                     continue
#         return a
    
    
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles)

        round = n//3
        for i in range(round):
            piles.pop(0)
        piles = piles[::-1]
        count= 0
        for i in range(len(piles)):
            if i%2 !=0:
                count+= piles[i]
        return count


                
            
            
        
        
        
        
        