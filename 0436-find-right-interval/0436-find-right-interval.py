class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        
        interval = sorted(intervals)
        ans = [-1] * n
        
        for i in range(n):
        
            left = 0
            right = n - 1
            while left <= right:
                mid = left + (right - left)//2
                
                if interval[mid][0] < intervals[i][1]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            if left < n:
                ans[i] = interval[left][2]
                             
        return ans
            
            
        
            