class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        max_ = 0 

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
        
            max_ = max(max_, zeros + ones)
        
        return max_
            