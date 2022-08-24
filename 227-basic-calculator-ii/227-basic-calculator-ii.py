class Solution:
    def calculate(self, s: str) -> int:
        
        count, prev, cur, ans = 0,0,0,0
        operation = '+'
        
        while count < len(s):
            
            char = s[count]
            if char.isdigit():

                while count<len(s) and s[count].isdigit():
                     cur = cur * 10 + int(s[count])
                     count += 1
                    
                count -= 1
                     
                if operation == '+':
                    ans += cur
                    prev = cur

                elif operation == '-':
                    ans -= cur
                    prev = -cur

                elif operation == '*':
                    ans -= prev
                    ans += prev*cur
                    prev = cur * prev

                else:
                    ans -= prev
                    ans += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif char != ' ':
                     operation = char
            count += 1
        return ans
            
                
            
        
        
            

            
            