class Solution:
    def minimumSum(self, num: int) -> int:
        
        li = list(map(int,str(num)))
        li.sort()
        new1 = str(li[0]) + str(li[3])
        new2 = str(li[1]) + str(li[2])
        
        return int(new1) + int(new2)
        
        
        