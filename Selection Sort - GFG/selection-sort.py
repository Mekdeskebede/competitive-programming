#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        
        less = arr[i]
        idx = i
        
        for j in range(i+1,n):
            if less > arr[j]:
                less = arr[j] 
                idx = j
        arr[i],arr[idx] = arr[idx], arr[i]
        # return less, idx
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            self.select(arr,i)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends