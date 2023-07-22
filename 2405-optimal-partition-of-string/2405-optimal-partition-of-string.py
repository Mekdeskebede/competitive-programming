class Solution:
    def partitionString(self, s: str) -> int:
        
        unique = set()
        ans = 1
        
        for char in s:
            if char not in unique:
                unique.add(char)
            else:
                ans += 1
                unique = set()
                unique.add(char)
        return ans