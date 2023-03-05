class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

                
        arr_set = set(arr)
        missing = 0
        
        for i in range(1, max(arr_set)):
            if i not in arr_set:
                missing += 1
                if missing == k:
                    return i
                
        return max(arr_set) + k - missing
                
            