class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        add = 0
        for i in range(k):
            add += cardPoints[i]
        
        maxPoint = add
        prev = cardPoints[0]
        left = k - 1
        right = n-1
        while left >= 0:
            add += cardPoints[right] - cardPoints[left]
            left -= 1
            right -= 1
            maxPoint = max(maxPoint, add)
            
        return maxPoint