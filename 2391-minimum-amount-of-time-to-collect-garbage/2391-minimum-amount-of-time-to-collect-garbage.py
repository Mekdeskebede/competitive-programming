class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        ans = 0
        def helper(target):
            nonlocal ans
            ans += garbage[0].count(target)
            curr = 0
            for i in range(1,len(garbage)):
                curr += travel[i-1]
                if target in garbage[i]:
                    ans += curr + garbage[i].count(target)
                    curr = 0
        helper("M")
        helper("G")
        helper("P")
        
        return ans