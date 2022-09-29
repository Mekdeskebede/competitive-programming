class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
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
            
    
    