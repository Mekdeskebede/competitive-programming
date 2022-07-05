class Solution: 
    # temp = arr
    # i = 0
    result = []
    def select(self, arr,i):
        return min(arr[i:])
        
        
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(n):
            # print(self.select(arr,i))
            selected = self.select(arr,i)
             
            arr[arr.index(selected)] = arr[i]
            arr[i] = selected
            
            # arr[i], arr[arr.index(selected)] = arr[arr.index(selected)], arr[i]
        return arr
            
            
        