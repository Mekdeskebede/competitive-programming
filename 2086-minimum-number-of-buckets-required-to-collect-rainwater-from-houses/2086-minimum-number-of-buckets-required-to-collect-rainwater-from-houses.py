class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        count = 0
        length = len(street)
        street = list(street)
    
        for idx, val in enumerate(street):
            if val == 'H':
                if idx-1>=0 and street[idx-1]=='B':
                    continue
                elif idx + 1 < length and street[idx+1]=='.':
                    street[idx+1] = 'B'
                    count+=1
                    continue
                elif idx-1>=0 and street[idx-1]=='.':
                    street[idx-1] = 'B'
                    count+=1
                    continue
                else:
                    return -1

        return count 
        
        
        
        
        
        
        # stack = []
#         ans = 0
#         for i in range(len(street)):
            
#             if i == ".":
#                 continue
               
#             elif street[i] == "H" and not stack:
#                 stack.append(i)
                
#             elif street[i] == "H" and stack and i - stack[-1] > 1 :
#                 print(i - stack[-1])
#                 ans += i - stack[-1] -1
#                 stack = []
#             elif street[i] == "H" and stack and i - stack[-1] <= 1:
#                 stack.pop()
#                 stack.append(i)
            
                
#         return -1 if ans == 0 else ans