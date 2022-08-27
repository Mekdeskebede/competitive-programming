class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        binary = '0'
        
        while (n > 0):
            
            temp = binary
            temp = temp[::-1]
            list_temp = []
            
            for i in range(len(temp)):
                
                if temp[i] == "0":
                    list_temp.append('1')
                else:
                    list_temp.append('0')
                
            binary = binary + '1' + ''.join(list_temp)
            n -= 1
            
       
        return binary[k-1]
    