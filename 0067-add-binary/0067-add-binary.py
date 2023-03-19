class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        diff = abs(len(a)-len(b))
        if len(a) >= len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a

        for i,j in zip(reversed(a), reversed(b)):
            total = int(i) + int(j) + carry
            
            carry = total // 2
            ans += str(total % 2)

        if carry == 1:
            ans += "1"
        return ans[::-1]