class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    
        ans = []
        candidates = [i+1 for i in range(n)]
        
        def backTrack(candidate,arr):
            if len(arr) == k:
                print(arr)
                ans.append(arr[:])
                return
            
            for num in candidates[candidate:]:
                arr.append(num)
                backTrack(candidate+1,arr)
                arr.pop()
                candidate += 1
        backTrack(0,[])
        return ans