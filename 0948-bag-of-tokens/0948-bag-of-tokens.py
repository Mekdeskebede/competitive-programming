class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        score = 0
        maxScore = 0
        l = 0
        r = len(tokens) -1
        
        while l <= r :
            
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                maxScore = max(maxScore, score)
            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
                
        return maxScore
                