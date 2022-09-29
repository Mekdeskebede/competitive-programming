class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
#         maxLength = 0

#         minQueue = deque()
#         maxQueue = deque()
        
        
#         i,j = 0,0
#         n = len(nums)
        
#         while j < n:
#             # We only want bigger elements in maxQueue
#             while len(maxQueue) > 0 and maxQueue[-1] < nums[j]: maxQueue.pop()
#             maxQueue.append(nums[j])
            
#             # We only want smaller elements in minQueue
#             while len(minQueue) > 0 and minQueue[-1] > nums[j]: minQueue.pop()
#             minQueue.append(nums[j])
            
#             # Make sure the maximum absolute difference is <= limit
#             while len(maxQueue) > 0 and len(minQueue) > 0 and maxQueue[0] - minQueue[0] > limit:
#                 if maxQueue[0] == nums[i]: maxQueue.popleft()
#                 if minQueue[0] == nums[i]: minQueue.popleft()
#                 i += 1
                
#             maxLength = max(maxLength, j - i + 1)
#             j += 1
        
#         return maxLength
        ans = 0
        right , left = 0, 0
        maxHeap, minHeap = [], []
        
        
        while right < len(nums):
            while maxHeap and maxHeap[-1] < nums[right]:
                maxHeap.pop()
            maxHeap.append(nums[right])
            
            while minHeap and minHeap[-1] > nums[right]:
                minHeap.pop()
            minHeap.append(nums[right])
                
            while maxHeap and minHeap and maxHeap[0] - minHeap[0] > limit:
                if maxHeap[0] == nums[left]: 
                    maxHeap.pop(0)
                if minHeap[0] == nums[left]: 
                    minHeap.pop(0)
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans
            
    
    