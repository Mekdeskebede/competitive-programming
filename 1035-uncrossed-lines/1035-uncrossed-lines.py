class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def dfs(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0
            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]
            if nums1[idx1] == nums2[idx2]:
                dp[(idx1,idx2)] = 1 + dfs(idx1-1,idx2-1)
            else:
                dp[(idx1,idx2)] = max(dfs(idx1-1,idx2), dfs(idx1,idx2-1))
                
            return dp[(idx1,idx2)]
            
        return dfs(len(nums1)-1,len(nums2)-1)