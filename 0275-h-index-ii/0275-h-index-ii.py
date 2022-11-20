class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        h = n - 1
        ans = 0
        while l <= h:
            mid = l + (h - l)//2
            if citations[mid] >= n-mid:
                ans = n - mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
