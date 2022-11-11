class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        valid = {"6":"9", "9":"6", "0":"0", "1":"1", "8":"8"}
        l = 0
        r = len(num)-1
        
        while l <= r:
            if num[r] in valid and num[l]==valid[num[r]]:
                    l += 1
                    r -= 1
            else:
                return False
            
        return True
            