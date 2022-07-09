class Solution(object):
    
    
    def sorting(self,a):
    # to sort an array
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j+1] < a[j]:
                    a[j+1],a[j] = a[j],a[j+1]

                else:
                    continue
        return a
    
    def checkArithmeticSubarrays(self, nums, l, r):
        
        
        arithmetic = []
        temp = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp = self.sorting(temp)
            differnce = 0
            check = True
            print(temp)
            for j in range(len(temp)-1):
                if j == 0:
                    differnce = temp[j+1] - temp[j]
                elif temp[j+1] - temp[j] != differnce:
                    check = False
                    break
            arithmetic.append(check)

        return arithmetic