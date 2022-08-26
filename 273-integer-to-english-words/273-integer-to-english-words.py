class Solution:
    def numberToWords(self, num: int) -> str:
        
#         thuosands = ['', 'Thousand', 'Million', 'Billion']
        
#         tens = ['','', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety' ]
        
#         oneToNineteen = ['','One','Two', 'Three','Four','Five','Six','Seven','Eight ','Nine', 'Ten','Eleven','Twelve','thirteen','Fourteen', 'Fifteen','Sixteen', 'Seventeen', 'Eighteen',' Nineteen']
        
#         def numToWord(num):
#             if num == 0:
#                 return 'Zero'
#             idex = 0
            
#             while num > 0:
#                 if num % 1000 != 0:
                    
            # This approach handles the number in 3 digit chunks. Let's start by creating some maps of english words - ones, tens, yuck, and mult
        #   These have aligned indecies. ones[1] = "one". tens[4] = "forty".
        #   the 'yuck' map will help us with teen numbers that don't follow the usual pattern
        #   and the 'mult' map will help us with multiples of thousands
        
        # First, break the input into a list. We're going to then look at that list in 3 digit chunks. This is because three hundred and forty two thousand requires
        # the same processing as three hundred and forty two - just with a thousand thrown on the end. The same goes for million and billion
        
        # The function thous_group will handle these 3 -digit chunks
        #   First handle the hundreds - located at the first digit (group[0]). If the digit is 0, we add nothing, other wise we add one[digit] plus 'hundred'
        #   Then we can check for teens. If the second digit (group[1]) is 1, we know we can just add the third digit's teen value
        #   If not a teen, we can add the tens[at group[1]] and ones[at group[2]] directly
        #   Finally, we can add the thousands, which is inferred from the input parameter mulitplier which we will set in our main loop later
        #       - Note that we only add a thousands suffix if there is actually an output! The number 1,000,000 is not written One Million Zero Thousand
        
        # Once the function works (test it out with some 3 digit numbers), we can write our main loop that calls the function on different chunks of the input num
        #   We will start at the end of the number and work our way to the front. The iterator i keeps track of our place, and the multiplier variable keeps track of which
        #   multiple of 'thousand' we are on.
        #   We can call our function on these three digit chunks, adding their output each time.
        #   However, if the last chunk does not have 3 digits (ex. 12,345) then we can simply pad it out with some zeroes to make it 3 digits -> 012,345
        output = ''
        
        # Handle zero case
        if num == 0: return 'Zero'
        
        # Create mappings to english words
        ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine']
        tens = ['','',' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        yuck = [' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        mult = ['', ' Thousand', ' Million', ' Billion']
        
        # Function that handles three digits at a time
        def thous_group(group, multiplier):
            out = ''
            
            # Handle Hundreds
            if group[0] != 0:
                out = ones[group[0]] + ' Hundred'
            
            # Handle teen numbers
            if group[1] == 1:
                out += yuck[group[2]]
            
            # Handle the tens and ones (if not teens)
            else:
                out += tens[group[1]] +  ones[group[2]]
            
            # Handle multiplier (thousand, million, ...)
            if out: out += mult[multiplier]
                
            return out
        
        # Turn the input number into a list of integer digits
        num = list(str(num))
        num = [int(x) for x in num]
        
        # Loop through 3 digit groups
        i = len(num)
        multiplier = 0
        while i > 0:
            # If there are fewer than 3 digits left, add buffer 0s to it
            if i - 3 < 0: 
                num = abs(i-3)*[0] + num
                i += abs(i-3)
            
            # Use the helper function to return the string for this group
            output = thous_group(num[i-3:i], multiplier) + output
            i -= 3
            multiplier += 1
            
        return output.strip()