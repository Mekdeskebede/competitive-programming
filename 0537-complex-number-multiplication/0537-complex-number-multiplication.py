class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        num1_real, num1_imaginary = num1.split("+")
        num2_real, num2_imaginary = num2.split("+")
   
        num1_real = int(num1_real)
        num2_real = int(num2_real)
        num1_imaginary = int(num1_imaginary[:-1])
        num2_imaginary = int(num2_imaginary[:-1])
        
        real = num1_real * num2_real - num1_imaginary * num2_imaginary
        imaginary = num1_imaginary * num2_real + num2_imaginary * num1_real
        
        res = f"{real}+{imaginary}i"
        
        return res