class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        
        if n < 3:
            return False
        if arr[0] > arr[1]:
            return False
        
        increasing = True
        prev = arr[0]
        
        for i in range(1,n):
            
            if arr[i] < prev and increasing:
                increasing = False
                
            elif arr[i] == prev:
                return False
            
            elif not increasing and arr[i] >= prev:
                return False
            
            prev = arr[i]
    
        return increasing == False