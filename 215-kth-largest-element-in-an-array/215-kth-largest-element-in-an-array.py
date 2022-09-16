class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        new_list = nums
        heapq.heapify(new_list)
        
        while len(nums) > k:
            heapq.heappop(new_list)
            
        return new_list[0]