class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li = list(s)
        
        if len(li) <= k:
            return s[::-1]
        else:
            ans = ""
            even = 0
            for i in range(0,len(s),k):
                
                temp = s[i:i+k]
                if even%2 == 0:
                    ans += temp[::-1]
                else:
                    ans += temp
                even += 1
                
            return ans
            
         