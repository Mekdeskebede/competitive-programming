class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_large = max(candies)
        ans = []
        
        for candy in candies:
            if candy + extraCandies >= curr_large:
                ans.append(True)
            else:
                ans.append(False)
        return ans