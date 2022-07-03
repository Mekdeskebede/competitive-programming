class Solution(object):
    def fizzBuzz(self, n):
        strarr =[]
        for i in range(n):
            i = i+1
            if i%3==0 and i%5==0:
                strarr.append("FizzBuzz")
            
            
            elif i%3==0:
                strarr.append("Fizz")
            elif i%5==0:
                strarr.append("Buzz")
            else:
                strarr.append(str(i))
        return strarr
            
          
       
        
        