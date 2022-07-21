class Solution(object):
    
    def is_Sorted(self, arr):
        check = 0
        i = 1
        while i < len(arr):
            if(arr[i] < arr[i - 1]):
                check = 1
            i += 1
        if not check:
            return True
        else: 
            return False
        
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxim = []
        for i in arr:
            maxim.append(i)
        result = []
        print(maxim)
        
        while not self.is_Sorted(arr):
            if maxim != []:
                m = max(maxim)
                maxim.pop(maxim.index(m))
                result.append(arr.index(m)+1)
                arr = arr[arr.index(m)::-1] + arr[arr.index(m)+1:]
                
                arr = arr[len(maxim)::-1] + arr[len(maxim)+1:]
                result.append(len(maxim)+1)
                print(arr)
        
        return result
            
            
            
            
         