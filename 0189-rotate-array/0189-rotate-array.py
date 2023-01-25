class Solution:
    
    def reverser(self,arr,left,right):
        arr[left:right] = arr[left:right][::-1]
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        n = len(nums)
        k = k%n
        left = 0
        right = n
        
        self.reverser(nums,left,right)
        self.reverser(nums,0,k)
        self.reverser(nums,k,n)
        
        
        