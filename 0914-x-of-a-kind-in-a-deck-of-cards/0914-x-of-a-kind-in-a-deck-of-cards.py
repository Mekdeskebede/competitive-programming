class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcd(num1,num2):
            if num2 == 0:
                return num1
            return gcd(num2,num1%num2)
        
        count = Counter(deck)
        values = list(count.values())
        n = len(values)
        if n < 2 and values[0] == 1:
            return False
        prev = values[0]
        
        for i in range(1,len(values)):
            if gcd(prev,values[i]) <= 1:
                return False
            prev = gcd(prev,values[i])
            
        return True