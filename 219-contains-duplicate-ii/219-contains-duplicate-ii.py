class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        visited = {}
        for idx, val in enumerate(nums):
            if val in visited:
                if abs(visited[val] - idx) <= k:
                    return True
                else:
                    visited[val] = idx
            else:
                visited[val] = idx
        return False
            