class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0: 
            return 'Zero'

        result = ''
        
      
        ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine']
        tens = ['','',' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        Twenty = [' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        Thousands = ['', ' Thousand', ' Million', ' Billion']
        
        def thous_group(team, multiplier):
            out = ''
            
          
            if team[0] != 0:
                out = ones[team[0]] + ' Hundred'
            
            if team[1] == 1:
                out += Twenty[team[2]]
            
            else:
                out += tens[team[1]] +  ones[team[2]]
            
            # Handle multiplier (thousand, million, ...)
            if out: out += Thousands[multiplier]
                
            return out
        
       
        num = list(str(num))
        num = [int(x) for x in num]
        
       
        i = len(num)
        multiplier = 0
        while i > 0:

            if i - 3 < 0: 
                num = abs(i-3)*[0] + num
                i += abs(i-3)
            
         
            result = thous_group(num[i-3:i], multiplier) + result
            i -= 3
            multiplier += 1
            # result = result
        return result.strip()